"""
Day 13 — Collections Drills (Tuples & Sets, with a small Dict recap)
Author: Santosh Menon
Repo path suggestion: algorithmic-thinking/day13_collections.py

What this file captures from Day 13:
- Tuple basics & unpacking
- Tuples inside collections (students with (name, score, grade))
- Honor roll filter + average of honors
- Set operations (union, intersection, difference, symmetric difference)
- Real-world set use cases (deduplicate emails, attendance compare, membership test)
- Mini-challenge: multi_enrolled(courses) → returns (multi_enrolled_set, all_students_set)
- Small dict recap: low-stock summary (ties back to Day 10)

Run this file to see demo outputs for each section.
"""

# -----------------------------
# Section 1: Tuples & Unpacking
# -----------------------------

students = [
    ("Alice", 91, "A"),
    ("Bob", 72, "B"),
    ("Charlie", 85, "A"),
    ("David", 66, "C"),
    ("Ella", 95, "A"),
]


def honor_roll(students, min_score=85, required_grade="A"):
    """Return (honor_list, count, average_score_of_honors)."""
    honors = []
    total = 0
    count = 0
    for name, score, grade in students:
        if score >= min_score and grade == required_grade:
            honors.append((name, score, grade))
            total += score
            count += 1
    avg = round(total / count, 2) if count > 0 else 0.0
    return honors, count, avg


# ---------------------------------
# Section 2: Sets — Core Operations
# ---------------------------------

def demo_set_operations():
    store_a = {"apples", "bananas", "oranges", "bread"}
    store_b = {"bread", "milk", "eggs", "bananas"}

    union_items = store_a | store_b
    intersection_items = store_a & store_b
    difference_a_b = store_a - store_b
    symmetric_diff = store_a ^ store_b

    return {
        "union": union_items,
        "intersection": intersection_items,
        "difference_a_minus_b": difference_a_b,
        "symmetric_difference": symmetric_diff,
    }


# ----------------------------------------------------------
# Section 3: Sets — Real-World Patterns & Quick Mini-Drills
# ----------------------------------------------------------

def deduplicate_emails(emails):
    """Return a set of unique emails (deduplicate)."""
    return set(emails)


def attendance_compare(db_students, attendance_today):
    """Return (present, absent, unknown) using set logic."""
    present = db_students & attendance_today
    absent = db_students - attendance_today
    unknown = attendance_today - db_students
    return present, absent, unknown


def fast_membership_check(allowed_ids, user_input):
    """Return True if user_input in allowed_ids set."""
    return user_input in allowed_ids


# --------------------------------------------------------------------
# Section 4: Mini-Challenge — Students in Multiple Courses (Tuples+Sets)
# --------------------------------------------------------------------

courses = [
    ("CS7637", "Thompson", {"Ava", "Ben", "Clara"}),
    ("CS7641", "Isbell",   {"Ben", "David", "Ella"}),
    ("CS6601", "Goel",     {"Clara", "Frank", "Grace"}),
]


def multi_enrolled(courses_list):
    """Return (students_in_multiple_courses, all_unique_students).

    Uses the seen_once / seen_multiple set pattern.
    """
    all_students = set()
    seen_once = set()
    seen_multiple = set()

    for course_name, instructor, students_set in courses_list:
        for s in students_set:
            all_students.add(s)
            if s in seen_once:
                seen_multiple.add(s)
            else:
                seen_once.add(s)

    return seen_multiple, all_students


# -----------------------------------
# Section 5: Small Dict Recap (Day 10)
# -----------------------------------

def low_stock_summary(groceries, threshold=3):
    """Return (low_dict, count) of items with qty <= threshold."""
    low = {item: qty for item, qty in groceries.items() if qty <= threshold}
    return low, len(low)


# -------------------------
# Run all demos if executed
# -------------------------

if __name__ == "__main__":
    print("=== Section 1: Tuples & Unpacking — Honor Roll ===")
    honors, count, avg = honor_roll(students, min_score=85, required_grade="A")
    for name, score, grade in honors:
        print(f" - {name} made the honor roll with {score} ({grade})")
    print(f"Total on honor roll: {count}")
    print(f"Average honor score : {avg}
")

    print("=== Section 2: Sets — Operations ===")
    ops = demo_set_operations()
    for key, val in ops.items():
        print(f"{key:20}: {sorted(list(val))}")
    print()

    print("=== Section 3: Sets — Real-World Drills ===")
    emails = ["a@gt.edu", "b@gt.edu", "a@gt.edu", "c@gt.edu", "b@gt.edu"]
    unique = deduplicate_emails(emails)
    print("Unique emails:", sorted(unique))

    db = {"Alice", "Bob", "Charlie", "David"}
    today = {"Alice", "Charlie", "Ella"}
    present, absent, unknown = attendance_compare(db, today)
    print("Present:", sorted(present))
    print("Absent:", sorted(absent))
    print("Unknown:", sorted(unknown))

    allowed = {"A100", "B200", "C300"}
    print("Access C300?", fast_membership_check(allowed, "C300"))
    print("Access Z999?", fast_membership_check(allowed, "Z999"))
    print()

    print("=== Section 4: Mini-Challenge — Multi-Enrolled ===")
    multi, all_people = multi_enrolled(courses)
    print("Students in multiple courses:", sorted(multi))
    print("All unique students        :", sorted(all_people))
    print()

    print("=== Section 5: Dict Recap — Low Stock Summary ===")
    groceries = {"apples": 5, "bananas": 2, "milk": 1, "bread": 4, "eggs": 3}
    low, low_count = low_stock_summary(groceries, threshold=3)
    print("Low-stock items:", low)
    print("Low-stock count:", low_count)
