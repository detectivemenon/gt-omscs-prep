import numpy as np

students = np.array(["Ava", "Ben", "Clara", "David", "Ella"])
subjects = np.array(["Math", "Science", "English", "History"])

# Example scores (5 students × 4 subjects)
scores = np.array([
    [78, 82, 91, 85],
    [92, 88, 79, 95],
    [67, 74, 70, 72],
    [88, 82, 91, 85],
    [75, 80, 84, 89]
])

# Calculate averages and grades
averages = scores.mean(axis=1)
grades = np.where(averages >= 90, "A",
          np.where(averages >= 80, "B",
          np.where(averages >= 70, "C", "D")))

# ---- SIMPLE, CLEAN LOOP ----
for name, avg, grade in zip(students, averages, grades):
    print(f"{name:6s} → Avg = {avg:.1f}, Grade = {grade}")

# ---- TOP 3 STUDENTS ----
N = 3
top_indices = np.argsort(averages)[::-1][:N]
print("\nTop 3 Students:")
for i in top_indices:
    print(f"{students[i]} → {averages[i]:.2f}")

# ---- SUBJECT STATS ----
print("\nSubject Statistics:")
for j, subject in enumerate(subjects):
    col = scores[:, j]
    print(f"{subject:8s} → Mean:{col.mean():.1f} Max:{col.max()} Min:{col.min()}")