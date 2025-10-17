"""
Day 14 — Modular Thinking & Problem Decomposition
Author: Santosh Menon
Repo: gt-omscs-prep (algorithmic-thinking/day14_modular_thinking.py)

Goal:
- Practice breaking problems into small, reusable functions.
- Practice chaining functions and returning structured data.
- Light intro to error handling with try/except.
- Reuse collections (lists, tuples, dicts, sets) in a modular way.

Instructions:
- Fill each TODO in sequence.
- Run each mini-challenge independently inside `if __name__ == "__main__":`.
- Keep outputs clean, deterministic, and readable.
"""


# ---------------------------------------------------------------------------
# Mini-Challenge 1: Student Grades Aggregator
# ---------------------------------------------------------------------------
# Input example (you can modify):
# students = [
#     ("Alice", [92, 88, 95]),
#     ("Bob",   [76, 81, 70]),
#     ("Cleo",  [65, 72, 68]),
# ]
#
# Tasks:
#   1) compute_average(scores) -> float
#   2) assign_grade(avg) -> str   (A/B/C etc. — you decide the thresholds)
#   3) generate_report(students) -> list[str] or dict[str, (avg, grade)]
#   4) (Bonus) class_average(report) -> float
#
# Tips:
#   - Keep functions pure (no prints), and do printing only in main().
#   - Use round(avg, 2) for clean output.
#   - Choose simple thresholds (e.g., >= 90: A, >= 80: B, ...).


def compute_average(scores):
    """Return the average of a non-empty list of numeric scores.
    TODO: implement (sum + len). Guard against empty list if you want.
    """
    # TODO
    pass


def assign_grade(avg):
    """Return a letter grade based on the numeric average.
    TODO: implement simple thresholds, e.g., A/B/C/D/F.
    """
    # TODO
    pass


def generate_report(students):
    """Return a structure (list or dict) mapping student -> (average, grade).
    students: list[tuple[str, list[int|float]]]
    TODO: call compute_average() and assign_grade() for each student.
    """
    # TODO
    pass


def class_average(report):
    """Return the class average given the report from generate_report().
    If report is a dict: values may be (avg, grade). If list: decide structure.
    TODO: compute an overall mean of student averages.
    """
    # TODO
    pass


# ---------------------------------------------------------------------------
# Mini-Challenge 2: Safe Division Calculator (try/except)
# ---------------------------------------------------------------------------
# Tasks:
#   1) safe_divide(a, b) -> float | str
#      - Return the result if valid.
#      - If division by zero, return a helpful string message (not an exception).
#      - If types are invalid, handle gracefully (optional).
#   2) Add 2–3 simple test calls in main().


def safe_divide(a, b):
    """Divide a by b safely.
    TODO: use try/except ZeroDivisionError. Optionally handle TypeError.
    """
    # TODO
    pass


# ---------------------------------------------------------------------------
# Mini-Challenge 3: Modular Grocery Analyzer (composition)
# ---------------------------------------------------------------------------
# Revisit Day 10, but in a modular way (no inputs required for now).
#
# Example structure:
#   groceries = {"apples": 5, "bananas": 4, "milk": 2, "eggs": 1, "bread": 3}
#
# Tasks:
#   1) low_stock_items(groceries, threshold=3) -> dict[str, int]
#   2) restock_item(groceries, item, amount) -> None (mutates the dict)
#   3) generate_summary(groceries) -> str or dict with totals
#
# Notes:
#   - Keep functions pure except restock_item (by design).
#   - In main(), demonstrate calling low_stock_items() first,
#     then restock some items, then call generate_summary().


def low_stock_items(groceries, threshold=3):
    """Return a dict of items with qty <= threshold.
    TODO: implement using a dict comprehension.
    """
    # TODO
    pass


def restock_item(groceries, item, amount):
    """Increase the quantity of a single item in-place.
    TODO: guard if item not in dict; decide behavior (add or ignore).
    """
    # TODO
    pass


def generate_summary(groceries):
    """Return a readable summary string or a dict with totals.
    TODO: compute total unique items and total quantity. Format nicely.
    """
    # TODO
    pass


# ---------------------------------------------------------------------------
# Main Orchestrator
# ---------------------------------------------------------------------------
# Only use print statements here to show results.
# Fill the TODO blocks as you complete each mini-challenge.


if __name__ == "__main__":
    # ------------------------
    # 1) Student Grades Demo
    # ------------------------
    # TODO: define a students list; call generate_report() and class_average().
    # TODO: print the results in a clean, formatted way.
    pass

    # ------------------------
    # 2) Safe Division Demo
    # ------------------------
    # TODO: call safe_divide() with a few inputs (e.g., (10, 2), (3, 0), ("a", 2)).
    # TODO: print the results.
    pass

    # ------------------------
    # 3) Grocery Analyzer Demo
    # ------------------------
    # TODO: create a groceries dict.
    # TODO: call low_stock_items(), restock_item(), generate_summary().
    # TODO: print outputs before and after restocking to show change.
    pass
