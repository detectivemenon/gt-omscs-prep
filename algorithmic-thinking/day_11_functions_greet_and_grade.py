def greet(name, time_of_day):
    return f"Good {time_of_day}, {name}! Welcome to Python!"

def grade_student(name, score):
    if score >= 90:
        result = "Excellent!"
    elif score >= 75:
        result = "Good Job!"
    else:
        result = "Needs Improvement"
    return f"{name}, your performance is {result}"

if __name__ == "__main__":
    print(greet("Santosh", "evening"))
    print(grade_student("Santosh", 95))
