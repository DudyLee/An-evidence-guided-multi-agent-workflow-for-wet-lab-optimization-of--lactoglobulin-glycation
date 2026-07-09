"""Runs a meeting with LLM agents (Responses API)."""

import json
import os
import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from virtual_lab.agent import Agent
from virtual_lab.constants import CONSISTENT_TEMPERATURE, PUBMED_TOOL_DESCRIPTION, PUBMED_TOOL_NAME
from virtual_lab.prompts import (
    individual_meeting_agent_prompt,
    individual_meeting_critic_prompt,
    individual_meeting_start_prompt,
    SCIENTIFIC_CRITIC,
    team_meeting_start_prompt,
    team_meeting_team_lead_initial_prompt,
    team_meeting_team_lead_intermediate_prompt,
    team_meeting_team_lead_final_prompt,
    team_meeting_team_member_prompt,
)
from virtual_lab.utils import (
    count_discussion_tokens,
    count_tokens,
    get_summary,
    print_cost_and_time,
    run_pubmed_search,
    save_meeting,
)


def run_meeting(
    meeting_type: Literal["team", "individual"],
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    team_lead: Agent | None = None,
    team_members: tuple[Agent, ...] | None = None,
    team_member: Agent | None = None,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 0,
    temperature: float = CONSISTENT_TEMPERATURE,
    pubmed_search: bool = False,
    return_summary: bool = False,
    api_delay: float = 1.0,
    tool_choice: str | dict | None = None,
) -> str:
    """Runs a meeting using the Responses API instead of Assistants.

    :param meeting_type: The type of meeting.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param team_lead: The team lead for a team meeting (None for individual meeting).
    :param team_members: The team members for a team meeting (None for individual meeting).
    :param team_member: The team member for an individual meeting (None for team meeting).
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
    :param temperature: The sampling temperature.
    :param pubmed_search: Whether to include a PubMed search tool.
    :param return_summary: Whether to return the summary of the meeting.
    :param api_delay: The delay between API calls in seconds.
    :param tool_choice: The tool choice for the meeting.
    :return: The summary of the meeting (i.e., the last message) if return_summary is True, else None.
    """
    # Validate meeting type
    if meeting_type == "team":
        if team_lead is None or team_members is None or len(team_members) == 0:
            raise ValueError("Team meeting requires team lead and team members")
        if team_member is not None:
            raise ValueError("Team meeting does not require individual team member")
        if team_lead in team_members:
            raise ValueError("Team lead must be separate from team members")
        if len(set(team_members)) != len(team_members):
            raise ValueError("Team members must be unique")
    elif meeting_type == "individual":
        if team_member is None:
            raise ValueError("Individual meeting requires individual team member")
        if team_lead is not None or team_members is not None:
            raise ValueError(
                "Individual meeting does not require team lead or team members"
            )
    else:
        raise ValueError(f"Invalid meeting type: {meeting_type}")

    # Start timing the meeting
    start_time = time.time()

    # Set up client
    client = OpenAI(
        # base_url="https://openrouter.ai/api/v1",
        # api_key=os.getenv("OPENROUTER_API_KEY"),
        # OpenAI (original) config, keep for quick rollback:
        base_url="https://api.openai.com/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Set up team
    if meeting_type == "team":
        team = [team_lead] + list(team_members)
    else:
        team = [team_member] + [SCIENTIFIC_CRITIC]

    # Collect tools per agent (OpenAI schema) and a name->callable map for execution
    agent_to_tools_schema: dict[Agent, list[dict]] = {}
    all_tools_map: dict[str, object] = {}

    for agent in team:
        tools_schema = []
        for tool in agent.tools:
            if hasattr(tool, "to_openai_tool"):
                tools_schema.append(tool.to_openai_tool())
            elif hasattr(tool, "metadata"):
                tools_schema.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.metadata.name,
                            "description": tool.metadata.description,
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "input": {
                                        "type": "string",
                                        "description": "The search query input.",
                                    }
                                },
                                "required": ["input"],
                            },
                        },
                    }
                )
            # Store the callable tool for execution.
            if hasattr(tool, "metadata"):
                all_tools_map[tool.metadata.name] = tool

        if pubmed_search:
            tools_schema.append(PUBMED_TOOL_DESCRIPTION)

        agent_to_tools_schema[agent] = tools_schema

    # Discussion transcript and request history (for Responses input)
    discussion: list[dict[str, str]] = []
    history: list[dict[str, str]] = []

    # If team meeting, seed initial prompt into history & discussion
    if meeting_type == "team":
        initial_prompt = team_meeting_start_prompt(
            team_lead=team_lead,
            team_members=team_members,
            agenda=agenda,
            agenda_questions=agenda_questions,
            agenda_rules=agenda_rules,
            summaries=summaries,
            contexts=contexts,
            num_rounds=num_rounds,
        )
        history.append({"role": "user", "content": initial_prompt})
        discussion.append({"agent": "User", "message": initial_prompt})

    tool_token_count = 0

    def extract_text_and_tools(response) -> tuple[str, list]:
        """Extract plain text and tool calls from a Responses API response."""
        text_parts: list[str] = []
        tool_calls: list = []

        # Prefer output_text if present (schema/text-format cases)
        if getattr(response, "output_text", None):
            text_parts.append(response.output_text)

        for block in getattr(response, "output", []) or []:
            if getattr(block, "tool_calls", None):
                tool_calls.extend(block.tool_calls)

            content = getattr(block, "content", None) or []
            for c in content:
                # Responses content blocks expose .text or .text.value depending on SDK version
                if hasattr(c, "text"):
                    text_val = getattr(c.text, "value", c.text)
                    if text_val:
                        text_parts.append(text_val)

        return "\n".join([t for t in text_parts if t]), tool_calls

    def run_tool_calls(tool_calls: list) -> list[dict[str, str]]:
        """Execute LLM-requested tools and return tool outputs list."""
        outputs = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            args_raw = tool_call.function.arguments
            args_dict = json.loads(args_raw) if isinstance(args_raw, str) else args_raw

            print(f"Running tool: {tool_name} with arguments: {args_dict}")

            if tool_name == PUBMED_TOOL_NAME:
                output_text = run_pubmed_search(**args_dict)
            elif tool_name in all_tools_map:
                tool_obj = all_tools_map[tool_name]
                query_input = args_dict.get("input", args_dict.get("query", ""))
                try:
                    output_text = str(tool_obj(query_input))
                except Exception as e:
                    output_text = f"Error running tool {tool_name}: {e}"
            else:
                output_text = f"Error: Unknown tool '{tool_name}'"

            outputs.append({"tool_call_id": tool_call.id, "output": output_text})
        return outputs

    def call_agent(agent: Agent, prompt: str) -> str:
        """Invoke Responses API for a single agent turn and return its final text."""
        nonlocal tool_token_count

        # user prompt into history (for saved discussion)
        history.append({"role": "user", "content": prompt})
        discussion.append({"agent": "User", "message": prompt})

        effective_tool_choice = tool_choice

        if isinstance(tool_choice, dict) and "function" in tool_choice:
            available_tool_names = [
                t.metadata.name for t in agent.tools if hasattr(t, "metadata")
            ]
            if pubmed_search:
                available_tool_names.append(PUBMED_TOOL_NAME)
            if tool_choice["function"].get("name") not in available_tool_names:
                effective_tool_choice = None
        elif tool_choice == "required":
            has_tools = len(agent.tools) > 0 or pubmed_search
            if not has_tools:
                effective_tool_choice = None

        def _create_response():
            request_kwargs = {
                "model": agent.model,
                "temperature": temperature,
                "input": [{"role": "system", "content": agent.prompt}, *history],
            }

            tools_schema = agent_to_tools_schema.get(agent, [])
            if tools_schema:
                request_kwargs["tools"] = tools_schema
            if effective_tool_choice is not None:
                request_kwargs["tool_choice"] = effective_tool_choice

            return client.responses.create(**request_kwargs)

        # First call
        response = _create_response()
        text, tool_calls = extract_text_and_tools(response)

        # Handle tool calls; one execution round is sufficient for this workflow.
        if tool_calls:
            tool_outputs = run_tool_calls(tool_calls)
            tool_token_count += sum(count_tokens(t["output"]) for t in tool_outputs)

            tool_output_text = "Tool Output:\n\n" + "\n\n".join(
                t["output"] for t in tool_outputs
            )
            history.append({"role": "user", "content": tool_output_text})
            discussion.append({"agent": "User", "message": tool_output_text})

            if api_delay > 0:
                time.sleep(api_delay)

            response = _create_response()
            text, _ = extract_text_and_tools(response)

        return text

    # Loop through rounds
    for round_index in trange(num_rounds + 1, desc="Rounds (+ Final Round)"):
        round_num = round_index + 1

        for agent in tqdm(team, desc="Team"):
            if meeting_type == "team":
                if agent == team_lead:
                    if round_index == 0:
                        prompt = team_meeting_team_lead_initial_prompt(team_lead=team_lead)
                    elif round_index == num_rounds:
                        prompt = team_meeting_team_lead_final_prompt(
                            team_lead=team_lead,
                            agenda=agenda,
                            agenda_questions=agenda_questions,
                            agenda_rules=agenda_rules,
                        )
                    else:
                        prompt = team_meeting_team_lead_intermediate_prompt(
                            team_lead=team_lead,
                            round_num=round_num - 1,
                            num_rounds=num_rounds,
                        )
                else:
                    prompt = team_meeting_team_member_prompt(
                        team_member=agent, round_num=round_num, num_rounds=num_rounds
                    )
            else:
                if agent == SCIENTIFIC_CRITIC:
                    prompt = individual_meeting_critic_prompt(
                        critic=SCIENTIFIC_CRITIC, agent=team_member
                    )
                else:
                    if round_index == 0:
                        prompt = individual_meeting_start_prompt(
                            team_member=team_member,
                            agenda=agenda,
                            agenda_questions=agenda_questions,
                            agenda_rules=agenda_rules,
                            summaries=summaries,
                            contexts=contexts,
                        )
                    else:
                        prompt = individual_meeting_agent_prompt(
                            critic=SCIENTIFIC_CRITIC, agent=team_member
                        )

            if api_delay > 0:
                time.sleep(api_delay)

            agent_text = call_agent(agent=agent, prompt=prompt)
            discussion.append({"agent": agent.title, "message": agent_text})
            history.append({"role": "assistant", "content": f"{agent.title}: {agent_text}"})

            if round_index == num_rounds:
                break

    token_counts = count_discussion_tokens(discussion=discussion)
    token_counts["tool"] = tool_token_count

    print_cost_and_time(
        token_counts=token_counts,
        model=team_lead.model if meeting_type == "team" else team_member.model,
        elapsed_time=time.time() - start_time,
    )

    save_meeting(
        save_dir=save_dir,
        save_name=save_name,
        discussion=discussion,
    )

    if return_summary:
        return get_summary(discussion)
