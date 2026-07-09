"""Optional literature-query tools used during local workflow development.

The reviewer package does not include the LlamaIndex vector-store cache because
it contains retrieval artifacts derived from source literature. Structured
reviewer-facing evidence files are provided under ``data/paper_data/`` instead.
"""

from pathlib import Path


def setup_paper_query_tool(storage_dir: str | Path | None = None):
    """Return a LlamaIndex query tool when a local storage cache is available.

    Parameters
    ----------
    storage_dir:
        Optional path to a prebuilt LlamaIndex storage directory. If omitted,
        the function looks for ``data/paper_data/storage`` under the repository
        root. That directory is intentionally excluded from the reviewer
        package; see ``EXCLUDED_FILES.md``.
    """

    try:
        from llama_index.core import Settings, StorageContext, load_index_from_storage
        from llama_index.core.tools import QueryEngineTool, ToolMetadata
        from llama_index.embeddings.openai import OpenAIEmbedding
        from llama_index.llms.openai import OpenAI
    except ImportError as exc:
        raise ImportError(
            "The optional paper-query helper requires llama-index packages. "
            "The reviewer package exposes structured evidence files directly "
            "and does not require this helper for manuscript data review."
        ) from exc

    repo_root = Path(__file__).resolve().parents[2]
    storage_path = Path(storage_dir) if storage_dir is not None else repo_root / "data" / "paper_data" / "storage"
    storage_path = storage_path.expanduser().resolve()

    if not storage_path.exists():
        raise FileNotFoundError(
            f"LlamaIndex storage was not found at {storage_path}. "
            "This cache is intentionally excluded from the reviewer package; "
            "use data/paper_data/Paper_run_data.computed_V2.jsonl for the "
            "reviewer-facing structured evidence records."
        )

    Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.2)
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    storage_context = StorageContext.from_defaults(persist_dir=str(storage_path))
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(similarity_top_k=5)

    return QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="academic_paper_db",
            description=(
                "A specialized database of academic literature related to "
                "beta-lactoglobulin modification and glycation."
            ),
        ),
    )
