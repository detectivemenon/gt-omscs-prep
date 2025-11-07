# Day 19 – CSV Handling Basics
# Save as: data_handling/day19_csv_basics.py
# Goal: Practice reading, writing, and analyzing CSV files manually and via pandas.

# ---------------------------------------------------------------------------
# Part A: Reading CSV (Manual & csv.reader)
# ---------------------------------------------------------------------------

import csv
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent
CSV_PATH = DATA_DIR / "students.csv"   # placeholder CSV file

def read_csv_basic(filepath: Path):
    """Read a CSV file line-by-line using csv.reader"""
    try:
        with filepath.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath.name}")

# ---------------------------------------------------------------------------
# Part B: Writing CSV (csv.writer)
# ---------------------------------------------------------------------------

def write_csv(filepath: Path, data):
    """Write a list of lists to CSV"""
    with filepath.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Subject", "Score"])
        writer.writerows(data)
    print(f"CSV written successfully to {filepath.name}")

# ---------------------------------------------------------------------------
# Part C: Reading & Filtering CSV with pandas
# ---------------------------------------------------------------------------

def read_csv_pandas(filepath: Path):
    """Read CSV using pandas and show basic summary"""
    try:
        df = pd.read_csv(filepath)
        print("=== DataFrame Head ===")
        print(df.head())
        print("\n=== Summary ===")
        print(df.describe())
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath.name}")
        return pd.DataFrame()

# ---------------------------------------------------------------------------
# Part D: Mini Project – CSV Aggregator
# ---------------------------------------------------------------------------

def summarize_scores(filepath: Path):
    """Compute average score per subject using pandas"""
    df = pd.read_csv(filepath)
    summary = df.groupby("Subject")["Score"].mean().round(2)
    print("\n=== Average Score per Subject ===")
    print(summary)
    return summary

# ---------------------------------------------------------------------------
# Smoke Test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sample_data = [
        ["Alice", "Math", 90],
        ["Bob", "Science", 85],
        ["Cathy", "Math", 88],
        ["David", "History", 92],
    ]

    write_csv(CSV_PATH, sample_data)
    print("\nReading CSV manually:")
    read_csv_basic(CSV_PATH)

    print("\nReading CSV via pandas:")
    df = read_csv_pandas(CSV_PATH)

    print("\nRunning CSV aggregator:")
    summarize_scores(CSV_PATH)