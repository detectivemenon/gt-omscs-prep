# Day 21 – Matplotlib Basics
# File: data_handling/day21_matplotlib_basics.py

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Part A: Basic Plot (line plot)
# -----------------------------------------------------------

def demo_line_plot():
    # TODO: create x,y arrays and plot them
    x = np.arange(0, 6)
    y = x * 2
    plt.plot(x, y)
    plt.title("My Chart")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()
    pass

# -----------------------------------------------------------
# Part B: Multiple Lines, Labels, Legends
# -----------------------------------------------------------

def demo_multiple_lines():
    # TODO: plot two or three lines with legends
    # --- DATA ---
    x = np.array([0, 1, 2, 3, 4, 5])
    y1 = np.array([0, 1, 4, 9, 16, 25])
    y2 = np.array([0, 2, 3, 6, 12, 18])

    # --- PLOTTING ---
    plt.plot(x, y1, color="blue", linestyle="-", linewidth=2, marker="o", label="Squares")
    plt.plot(x, y2, color="red", linestyle="--", linewidth=2, marker="s", label="Doubles")

    # --- LABELS / TITLE ---
    plt.title("My First Matplotlib Multi-Line Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    # --- LEGEND & GRID ---
    plt.legend()
    plt.grid(True)

    # --- SHOW PLOT ---
    plt.show()
    pass

# -----------------------------------------------------------
# Part C: Bar Charts
# -----------------------------------------------------------

def demo_bar_chart():

        # --------------------------
        # Basic dataset
        # --------------------------
        subjects = ["Math", "Science", "English", "History"]
        scores = [85, 92, 78, 88]

        # --------------------------
        # 1) Basic bar chart
        # --------------------------
        plt.figure(figsize=(6, 4))
        plt.bar(subjects, scores)
        plt.title("Basic Bar Chart")
        plt.xlabel("Subjects")
        plt.ylabel("Scores")
        plt.show()

        # --------------------------
        # 2) Bar chart with colors + grid
        # --------------------------
        plt.figure(figsize=(6, 4))
        plt.bar(subjects, scores, color="skyblue")
        plt.title("Bar Chart with Colors & Grid")
        plt.xlabel("Subjects")
        plt.ylabel("Score")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.show()

        # --------------------------
        # 3) Horizontal bar chart
        # --------------------------
        plt.figure(figsize=(6, 4))
        plt.barh(subjects, scores, color="orange")
        plt.title("Horizontal Bar Chart")
        plt.xlabel("Score")
        plt.ylabel("Subject")
        plt.show()

        # --------------------------
        # 4) Individual colors on each bar
        # --------------------------
        plt.figure(figsize=(6, 4))
        plt.bar(subjects, scores,
                color=["red", "green", "blue", "purple"])
        plt.title("Bar Chart with Individual Colors")
        plt.xlabel("Subjects")
        plt.ylabel("Score")
        plt.show()

        # --------------------------
        # 5) Grouped Bar Chart (Side-by-Side)
        # --------------------------
        test1 = [85, 92, 78, 88]
        test2 = [80, 90, 82, 91]

        x = np.arange(len(subjects))
        width = 0.35

        plt.figure(figsize=(7, 4))
        plt.bar(x - width / 2, test1, width, label="Test 1")
        plt.bar(x + width / 2, test2, width, label="Test 2")

        plt.xticks(x, subjects)
        plt.title("Grouped Bar Chart (Side-by-Side)")
        plt.xlabel("Subject")
        plt.ylabel("Scores")
        plt.legend()
        plt.show()

        # --------------------------
        # 6) Stacked Bar Chart
        # --------------------------
        plt.figure(figsize=(7, 4))
        plt.bar(subjects, test1, label="Test 1")
        plt.bar(subjects, test2, bottom=test1, label="Test 2")

        plt.title("Stacked Bar Chart")
        plt.xlabel("Subject")
        plt.ylabel("Combined Score")
        plt.legend()
        plt.show()

        pass


# -----------------------------------------------------------
# Part D: Scatter Plot
# -----------------------------------------------------------

def demo_scatter():
    # TODO: scatter plot with colors/sizes
    import numpy as np
    import matplotlib.pyplot as plt

    # Sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([4, 2, 5, 7, 6])
    sizes = np.array([100, 200, 150, 300, 250])
    colors = np.array(["red", "blue", "green", "purple", "orange"])

    plt.scatter(x, y, s=sizes, c=colors, marker="o")

    plt.title("Scatter Plot Example")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.grid(True)
    plt.show()
    pass

# -----------------------------------------------------------
# Part E: Subplots (2x2)
# -----------------------------------------------------------

def demo_subplots():
    # TODO: create 2x2 grid of small charts
    # Make some x values
    x = np.linspace(0, 10, 200)

    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = x
    y4 = x ** 2

    # Create a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    fig.suptitle("Subplots Demo", fontsize=14)

    # Top-left: sine
    axes[0, 0].plot(x, y1)
    axes[0, 0].set_title("sin(x)")

    # Top-right: cosine
    axes[0, 1].plot(x, y2)
    axes[0, 1].set_title("cos(x)")

    # Bottom-left: line
    axes[1, 0].plot(x, y3)
    axes[1, 0].set_title("y = x")

    # Bottom-right: parabola
    axes[1, 1].plot(x, y4)
    axes[1, 1].set_title("y = x²")

    # Tight layout so titles don’t overlap
    plt.tight_layout()
    plt.show()
    pass

# -----------------------------------------------------------
# Smoke Test
# -----------------------------------------------------------

if __name__ == "__main__":
    print("Running Day 21 Matplotlib demos...")

    # Uncomment as you complete each part
    # demo_line_plot()
    # demo_multiple_lines()
    # demo_bar_chart()
    # demo_scatter()
    demo_subplots()