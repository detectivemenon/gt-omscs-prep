# Day 7 – Working with Dictionaries (key->list of numbers)

grades = {
    "Alice": [85, 90, 82],
    "Bob": [78, 81, 86],
    "Charlie": [92, 88, 95]
}

print("Per-student averages:")
for name, scores in grades.items():
    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)
    print(f"{name}: average={avg:.2f}")

print("\nTop performer by average:")
top_student = ""
highest_avg = 0.0

for name, scores in grades.items():
    total = 0
    for s in scores:
        total += s
    avg = total / len(scores)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print(f"Top performer: {top_student} ({highest_avg:.2f})")