"""
Day 15 — OOP Basics: Classes & Objects

Goals:
- Define a simple class with attributes
- Initialize instances using __init__
- Add instance methods (behavior)
- Practice creating and using objects
"""

# -------------------------------------------------
# 1) Class definition
# -------------------------------------------------
# -------------------------
#  SECTION 1: CLASS BASICS
# -------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_details(self):
        print(f"This car is a {self.year} {self.brand} {self.model}")

    wheels = 4

    def update_mileage(self, new_mileage):
        """Update the car's mileage."""
        self.mileage = new_mileage
        print(f"{self.brand} {self.model} mileage updated to {self.mileage} miles.")

car1 = Car("Toyota", "Camry", 2014)
car2 = Car("BMW", "Z4 M40i", 2025)
car3 = Car("Honda", "911", 2022)

garage = [car1, car2, car3]
for each in garage:
    each.show_details()

mycar = Car("Toyota", "Camry", 2021)
mycar.show_details()
mycar.update_mileage(30000)
mycar.update_mileage(42000)

#---------------- BANK ACCOUNT ---------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # notice the double underscore!

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance = ${self.__balance}")
        else:
            print("Deposit must be positive.")

    def get_balance(self):
        return self.__balance


# Create object
acct = BankAccount("Santosh", 1000)
acct.deposit(500)
print(acct.get_balance())

# Try to change balance directly (should fail silently)
acct.__balance = 999999
print("After direct change:", acct.get_balance())
#----------------------------------------------------
## CLASS AND STATIC METHODS:

class MathUtils:
    pi = 3.14159  # class variable

    @classmethod
    def circle_area(cls, radius):
        """Uses class data — notice cls instead of self."""
        return cls.pi * (radius ** 2)

    @staticmethod
    def add(a, b):
        """Utility function — no need for class or instance data."""
        return a + b


# Test them
print(MathUtils.circle_area(5))
print(MathUtils.add(10, 20))
#----------------------------------------------------
#-------- INHERITENCE -------------------------------
# Base class - defined above
# Subclass
class ElectricCar(Car):          # <-- inherits from Car
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)    # call base-class constructor
        self.battery_size = battery_size  # add a new property

    def charge(self):
        print(f"Charging the {self.brand} {self.model} {self.year}({self.battery_size}-kWh battery).")


# Create objects
tesla = ElectricCar("Tesla", "Model 3", 2015, 100)
tesla.show_details()   # inherited method
tesla.charge()         # subclass-specific method


#----------------------------------------------------
class Student:
    """
    Represents a student with basic academic info.
    """

    def __init__(self, name: str, student_id: str, gpa: float = 0.0):
        """
        Initialize a new Student.

        Args:
            name: Full name of the student
            student_id: Unique ID (string)
            gpa: Current GPA (0.0–4.0 scale)
        """
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.courses = []  # list of course names (strings)

    # -------------------------------------------------
    # 2) Instance methods (behavior)
    # -------------------------------------------------

    def info(self) -> str:
        """
        Returns a one-line summary of the student.
        """
        return f"{self.name} (ID: {self.student_id}) — GPA: {self.gpa:.2f}, Courses: {len(self.courses)}"

    def add_course(self, course_name: str) -> None:
        """
        Add a course to the student's record if not already present.
        """
        # TODO: Check for duplicates before appending
        # TODO: Append course_name to self.courses
        pass

    def update_gpa(self, new_gpa: float) -> None:
        """
        Update GPA if value is valid (0.0–4.0).
        """
        # TODO: Validate range before assigning to self.gpa
        pass

    def has_course(self, course_name: str) -> bool:
        """
        Returns True if the student has taken course_name.
        """
        # TODO: Return True/False based on membership in self.courses
        pass


# -------------------------------------------------
# 3) (Optional) A second class for later days
#    We'll use this in Day 16–18 to explore composition/inheritance.
# -------------------------------------------------
class Course:
    """
    Represents a course with a name and a roster of students.
    """

    def __init__(self, name: str, instructor: str):
        self.name = name
        self.instructor = instructor
        self.roster = []  # list of Student objects

    def add_student(self, student: Student) -> None:
        """
        Add a student object to the roster if not already present.
        """
        # TODO (Day 17): Prevent duplicates; maybe check by student_id
        pass

    def summary(self) -> str:
        """
        Returns a summary line with course name, instructor, and class size.
        """
        return f"{self.name} — Instructor: {self.instructor}, Enrolled: {len(self.roster)}"


# -------------------------------------------------
# 4) Demo block
#    Use this to manually test your class as you implement TODOs.
# -------------------------------------------------
if __name__ == "__main__":
    # Create two students
    s1 = Student(name="Alice Johnson", student_id="GT001", gpa=3.5)
    s2 = Student(name="Ben Carter", student_id="GT002", gpa=3.2)

    # Print initial info
    print(s1.info())
    print(s2.info())

    # TODO: Add a couple of courses to s1 and s2
    # s1.add_course("CS1332")
    # s1.add_course("CS1332")  # test duplicate handling
    # s2.add_course("CS7637")

    # TODO: Update GPAs and reprint info
    # s1.update_gpa(3.7)
    # s2.update_gpa(3.9)
    # print(s1.info())
    # print(s2.info())

    # Quick Course demo
    course = Course(name="CS1332", instructor="Prof. Smith")
    # TODO (Day 17): Add students to course.roster and print summary
    print(course.summary())