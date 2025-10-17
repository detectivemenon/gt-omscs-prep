# Day 7 – Nested Dictionaries (student -> subject -> score)

students = {
    "Alice":   {"math": 90, "science": 85, "english": 88},
    "Bob":     {"math": 75, "science": 80, "english": 72},
    "Charlie": {"math": 92, "science": 89, "english": 94}
}

print("Per-student averages:")
for name, subjects in students.items():
    total = 0
    count = 0
    for subject, score in subjects.items():
        total += score
        count += 1
    avg = total / count
    print(f"{name}: average={avg:.2f}")

print("\nBest subject per student:")
for name, subjects in students.items():
    best_subject = ""
    best_score = -1
    for subject, score in subjects.items():
        if score > best_score:
            best_score = score
            best_subject = subject
    print(f"{name}: best={best_subject} ({best_score})")

print("\nClass average in math:")
total_math = 0
count_math = 0
for name, subjects in students.items():
    total_math += subjects["math"]
    count_math += 1
print(f"Math average: {total_math / count_math:.2f}")