#!/usr/bin/env python3
"""
NetGlycate Analysis for β-Lactoglobulin A (β-LG-A)

This script parses a β-LG-A FASTA sequence and NetGlycate output,
then reports the top N glycation-susceptible lysine residues.

Usage:
  python netglycate_analysis.py --fasta <input.fasta> --results <netglycate.csv> --top <N>

Inputs:
  --fasta:   Path to β-LG-A FASTA file.
  --results: Path to NetGlycate results (CSV/TSV) with columns: Position, Residue, Probability/Score.
  --top:     (Optional) Number of top lysines to report (default: 5).
"""

import argparse
import csv
import os
import sys
from typing import List, Tuple

def parse_fasta(filepath: str) -> str:
    """
    Parse a FASTA file and return the sequence as a string.
    Raises an error if the file is not found or improperly formatted.
    """
    if not os.path.isfile(filepath):
        sys.exit(f"Error: FASTA file '{filepath}' not found.")
    sequence = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('>') or not line.strip():
                continue
            sequence.append(line.strip())
    if not sequence:
        sys.exit("Error: No sequence found in the FASTA file.")
    return ''.join(sequence)

def detect_delimiter(header_line: str) -> str:
    """
    Auto-detect delimiter based on header line.
    """
    if ',' in header_line:
        return ','
    elif '\t' in header_line:
        return '\t'
    else:
        sys.exit("Error: Could not determine delimiter (should be CSV or TSV).")

def parse_netglycate_output(filepath: str) -> List[Tuple[int, str, float]]:
    """
    Parse NetGlycate output CSV/TSV and return list of (position, residue, score).
    Handles basic errors and missing columns.
    """
    if not os.path.isfile(filepath):
        sys.exit(f"Error: Results file '{filepath}' not found.")
    with open(filepath, 'r') as f:
        header_line = f.readline()
        delimiter = detect_delimiter(header_line)
        header = [h.strip().lower() for h in header_line.strip().split(delimiter)]
        # Find required columns
        try:
            pos_idx = header.index("position")
            res_idx = header.index("residue")
            score_idx = header.index("probability") if "probability" in header else header.index("score")
        except ValueError:
            sys.exit("Error: Expected columns 'Position', 'Residue', and 'Probability' or 'Score' in header. "
                     "Please edit your CSV/TSV file to use these column names.")
        # Parse data
        reader = csv.reader(f, delimiter=delimiter)
        results = []
        for row in reader:
            try:
                position = int(row[pos_idx])
                residue = row[res_idx]
                score = float(row[score_idx])
                results.append((position, residue, score))
            except (ValueError, IndexError):
                continue
    if not results:
        sys.exit("Error: No NetGlycate predictions could be parsed from file.")
    return results

def print_top_lysines(results: List[Tuple[int, str, float]], top_n: int = 5):
    """
    Print the top N lysine residues with highest glycation score.
    """
    lysines = [r for r in results if r[1].upper() == 'K']
    if not lysines:
        print("No lysine residues found in NetGlycate results.")
        return
    sorted_lysines = sorted(lysines, key=lambda x: x[2], reverse=True)
    print(f"{'Position':<10}{'Residue':<10}{'Glycation Score':<18}")
    print('-'*38)
    for pos, res, score in sorted_lysines[:top_n]:
        print(f"{pos:<10}{res:<10}{score:<18.4f}")
    print("\nENGINEERING RECOMMENDATIONS:")
    print(" - Consider these lysines as primary candidates for glycation or mutation to reduce allergenicity.")
    print(" - Prioritize lysines with highest probability for experimental validation.")
    print(" - Map these positions onto 3D models to assess accessibility and functional impact.")
    print(" - Avoid targeting lysines critical for protein folding, ligand binding, or stability (see PDB 1BEB).")

def main():
    parser = argparse.ArgumentParser(description="Analyze NetGlycate results for β-LG-A")
    parser.add_argument('--fasta', required=True, help="Path to β-LG-A FASTA file")
    parser.add_argument('--results', required=True, help="Path to NetGlycate results CSV/TSV")
    parser.add_argument('--top', type=int, default=5, help="Number of top lysine sites to show (default=5)")

    args = parser.parse_args()

    sequence = parse_fasta(args.fasta)
    print(f"Loaded β-LG-A sequence ({len(sequence)} residues) from '{args.fasta}'.")

    results = parse_netglycate_output(args.results)
    print(f"Loaded {len(results)} predictions from '{args.results}'.")

    print("\nTop susceptible lysine residues for glycation:")
    print_top_lysines(results, args.top)

if __name__ == "__main__":
    main()