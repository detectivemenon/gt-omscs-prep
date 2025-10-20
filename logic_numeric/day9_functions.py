# Day 9 – Refactoring to Functions
# Purpose: Learn to write modular, reusable Python functions and combine them cleanly.

def compute_total(scores):
    """Return the total of a list of numbers."""
    total = 0
    for s in scores:
        total += s
    return total


def compute_average(scores):
    """Return the average of a list of numbers using compute_total()."""
    total = compute_total(scores)
    return total / len(scores)


def find_top_student(grades):
    """Find the student with the highest average score."""
    top_name = ""
    top_avg = 0
    for name, scores in grades.items():
        avg = compute_average(scores)
        if avg > top_avg:
            top_avg = avg
            top_name = name
    return top_name, top_avg


# --- main program ---
grades = {
    "Alice": [85, 90, 82],
    "Bob": [78, 81, 86],
    "Charlie": [92, 88, 95]
}

best_student, best_avg = find_top_student(grades)
print(f"Top performer: {best_student} ({best_avg:.2f})")