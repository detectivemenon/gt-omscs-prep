# Day 7 – Working with Collections: List of Lists (accumulators + averages)

grades = [
    ["Alice", 85, 90, 82],
    ["Bob", 78, 81, 86],
    ["Charlie", 92, 88, 95]
]

for record in grades:
    name = record[0]
    scores = record[1:]
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    print(f"{name}: total={total}, average={avg:.2f}")