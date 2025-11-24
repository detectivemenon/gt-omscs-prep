import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def demo_warmup_plots():
    """Quick warm-up: line, bar, scatter in one go."""

    # 1) Create some simple NumPy data
    x = np.arange(1, 6)  # [1 2 3 4 5]
    y1 = x * 2  # [2 4 6 8 10]
    y2 = x ** 2  # [1 4 9 16 25]

    # ---- Line plot ----
    plt.figure(figsize=(6, 4))
    plt.plot(x, y1, marker="o", label="y = 2x")
    plt.plot(x, y2, marker="s", label="y = x^2")
    plt.title("Line Plot – Two Simple Functions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ---- Bar chart ----
    plt.figure(figsize=(6, 4))
    plt.bar(x, y1)
    plt.title("Bar Chart – y = 2x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

    # ---- Scatter plot ----
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y2)
    plt.title("Scatter Plot – y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()


def demo_subplots():
    """Show two related plots side-by-side using subplots."""
    x = np.arange(1, 6)
    y1 = x * 2
    y2 = x ** 2

    # One figure, 1 row, 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Left subplot: y = 2x
    axes[0].plot(x, y1, marker="o")
    axes[0].set_title("y = 2x")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].grid(True)

    # Right subplot: y = x^2
    axes[1].plot(x, y2, marker="s")
    axes[1].set_title("y = x^2")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def student_performance_dashboard():
    """Mini-project: visualize simple student score data."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # ---- 1. DATA SETUP ----
    students = np.array(["Ava", "Ben", "Clara", "David", "Ella"])
    subjects = np.array(["Math", "Science", "English", "History"])

    # 5 students × 4 subjects
    scores = np.array([
        [78, 85, 90, 88],
        [92, 80, 75, 89],
        [67, 70, 72, 65],
        [88, 82, 91, 85],
        [75, 78, 85, 80]
    ])

    # ---- 2. Averages & Grades ----
    averages = scores.mean(axis=1)

    grades = np.where(
        averages >= 90, "A",
        np.where(averages >= 80, "B",
        np.where(averages >= 70, "C", "D"))
    )

    # ---- 3. Convert to Pandas for easy plotting ----
    df = pd.DataFrame(scores, columns=subjects)
    df["Student"] = students
    df["Average"] = averages
    df["Grade"] = grades

    # ---- 4. FIGURE LAYOUT ----
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # ---- 5. BAR CHART: Student Averages ----
    axes[0].bar(df["Student"], df["Average"], color="skyblue")
    axes[0].set_title("Average Score per Student")
    axes[0].set_xlabel("Student")
    axes[0].set_ylabel("Average Score")
    axes[0].grid(axis="y", linestyle="--", alpha=0.5)

    # ---- 6. LINE PLOT: Subject Averages ----
    subject_means = df[subjects].mean()

    axes[1].plot(subjects, subject_means, marker="o", linewidth=2)
    axes[1].set_title("Average Score per Subject")
    axes[1].set_xlabel("Subject")
    axes[1].set_ylabel("Mean Score")
    axes[1].grid(True)

    # ---- 7. Render Plots ----
    plt.tight_layout()
    plt.show()

    # ---- 8. Print Summary Table ----
    print("\n=== STUDENT SUMMARY ===")
    for i in range(len(students)):
        print(f"{students[i]:6s} → Avg={averages[i]:.1f}, Grade={grades[i]}")


if __name__ == "__main__":
    #demo_warmup_plots()
    #demo_subplots()
    student_performance_dashboard()
