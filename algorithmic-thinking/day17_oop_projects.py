# Day 17 – OOP Mini-Projects: Integration & Real-World Simulation
# Save this file as: algorithmic-thinking/day17_oop_projects.py
# Tip: Run this file directly for quick smoke tests while you build each section.

# ---------------------------------------------------------------------------
# Mini-Project 1: Bank System (Encapsulation + Composition)
# Classes: Bank, Account
# Features:
#   - Bank: create_account(owner, initial=0), get_account(owner), total_deposits(), summary()
#   - Account: deposit(amount), withdraw(amount), get_balance() [balance should be private]
# TODOs:
#   1) Implement Account with __balance as a private attribute.
#   2) Implement safe deposit/withdraw with simple validation.
#   3) Implement Bank that stores multiple Account objects (composition).
#   4) Write a tiny smoke-test in __main__.
# ---------------------------------------------------------------------------

class Account:
    def __init__(self, owner: str, initial: float = 0.0):
        self.owner = owner
        self.__balance = float(initial)

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def get_balance(self) -> float:
        return self.__balance

    def show_account_details(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.__balance}")

    def transfer(self, to_account: "Account", amount: float) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            to_account.deposit(amount)
            print(f"Transferred ${amount} from {self.owner} to {to_account.owner}")
        else:
            print("Transfer failed: insufficient funds or invalid amount.")

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={getattr(self, '_Account__balance', 0.0):.2f})"

class Bank:
    def __init__(self, name: str):
        self.name = name
        self._accounts = {}  # key: owner (str) -> value: Account

    def create_account(self, owner: str, initial: float = 0.0):
        if owner in self._accounts:
            print(f"[Bank:{self.name}] Account for {owner} already exists.")
            return self._accounts[owner]
        acc = Account(owner, initial)
        self._accounts[owner] = acc
        print(f"[Bank:{self.name}] Created account for {owner} with initial ${initial}.")
        return acc

    def get_account(self, owner: str):
        return self._accounts.get(owner)

    def total_deposits(self) -> float:
        return sum(acc.get_balance() for acc in self._accounts.values())

    def summary(self) -> str:
        lines = [f"=== Bank Summary: {self.name} ==="]
        if not self._accounts:
            lines.append("(no accounts)")
        else:
            for owner, acc in self._accounts.items():
                lines.append(f"- {owner}: ${acc.get_balance():.2f}")
            lines.append(f"Total on deposit: ${self.total_deposits():.2f}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Mini-Project 2: Fleet Management (Inheritance + Polymorphism + Composition)
# Base class: Vehicle(brand, model)
# Subclasses: Car, ElectricCar, Truck
# Fleet holds a collection of Vehicle objects.
# Features:
#   - Each subclass implements fuel_type() differently.
#   - Fleet: add_vehicle(v), display_all(), filter_by_brand(brand)
# TODOs:
#   1) Implement Vehicle with show_details().
#   2) Implement subclasses overriding fuel_type() and optionally show_details().
#   3) Implement Fleet methods.
#   4) Add a tiny smoke-test in __main__.
# ---------------------------------------------------------------------------

class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def fuel_type(self) -> str:
        # TODO: default fuel type or raise NotImplementedError
        return "UNKNOWN"

    def show_details(self) -> str:
        return f"{self.brand} {self.model} | Fuel: {self.fuel_type()}"


class Car(Vehicle):
    def fuel_type(self) -> str:
        # TODO: return typical car fuel (e.g., 'Gasoline')
        return "Gasoline"


class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, battery_kwh: int):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

    def fuel_type(self) -> str:
        return "Electric"

    def show_details(self) -> str:
        base = super().show_details()
        return f"{base} | Battery: {self.battery_kwh} kWh"


class Truck(Vehicle):
    def fuel_type(self) -> str:
        # TODO: return e.g., 'Diesel'
        return "Diesel"


class Fleet:
    def __init__(self, name: str):
        self.name = name
        self._vehicles = []  # list[Vehicle]

    def add_vehicle(self, v: Vehicle):
        if not isinstance(v, Vehicle):
            raise TypeError("Only Vehicle instances can be added to the fleet.")
        self._vehicles.append(v)

    def display_all(self) -> str:
        if not self._vehicles:
            return f"=== Fleet: {self.name} ===\n(no vehicles)"
        lines = [f"=== Fleet: {self.name} ==="]
        for v in self._vehicles:
            # Polymorphism in action: each subclass's show_details() is used
            lines.append(v.show_details())
        return "\n".join(lines)

    def filter_by_brand(self, brand: str):
        return [v for v in self._vehicles if v.brand.lower() == brand.lower()]


# ---------------------------------------------------------------------------
# Mini-Project 3: Student Grade System (Encapsulation + Composition)
# Classes: Student(name) and Grade(subject, score)
# Features:
#   - Student.add_grade(Grade), Student.gpa(), Student.display_transcript()
#   - GPA = simple average of scores for now.
# TODOs:
#   1) Implement Grade.
#   2) Implement Student with a list of Grade objects.
#   3) Implement gpa() and display_transcript().
#   4) Add a tiny smoke-test in __main__.
# ---------------------------------------------------------------------------

class Grade:
    def __init__(self, subject: str, score: float):
        self.subject = subject
        self.score = float(score)

    def __repr__(self):
        return f"Grade(subject={self.subject!r}, score={self.score:.1f})"


class Student:
    def __init__(self, name: str):
        self.name = name
        self._grades = []  # list[Grade]

    def add_grade(self, grade: Grade):
        # TODO: append grade after simple validation (0 <= score <= 100)
        if not isinstance(grade, Grade):
            raise TypeError("Only Grade instances can be added to Student.")
        self._grades.append(grade)

    def gpa(self) -> float:
        # TODO: compute and return average score (0 if no grades)
        if not self._grades:
            return 0.0
        total = sum(g.score for g in self._grades)
        return round(total / len(self._grades), 2)

    def display_transcript(self) -> str:
        # TODO: return formatted transcript with each grade + GPA
        lines = [f"=== Transcript: {self.name} ==="]
        for g in self._grades:
            lines.append(f"{g.subject}: {g.score:.1f}")
        lines.append(f"GPA: {self.gpa():.2f}")
        return "\n".join(lines)

# ---------------------------------------------------------------------------
# Smoke tests (run this file directly to check your progress step-by-step)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    acc1 = Account("Santosh", 100)
    acc1.deposit(50)
    acc1.withdraw(30)

    acc1.show_account_details()  # 👈 calls your new method
    acc1 = Account("Santosh", 500)
    acc2 = Account("Saritha", 300)

    acc1.transfer(acc2, 150)

    print(acc1.show_account_details())
    print(acc2.show_account_details())

    print(f"Final Balance (via getter): ${acc1.get_balance()}")
    print(acc1.get_balance())  # ✅ works fine
    print("[Mini-Project 1] Bank System smoke test...")
    # TODO: create a Bank, add two Accounts, deposit/withdraw, print summary
    print("\n[Mini-Project 1] Bank System smoke test...")
    bank = Bank("GT Credit Union")
    s1 = bank.create_account("Santosh", 200.0)
    s2 = bank.create_account("Saritha", 300.0)
    bank.create_account("Santosh", 999.0)  # should warn and return existing

    s1.deposit(50)     # 200 -> 250
    s2.withdraw(40)    # 300 -> 260
    s1.transfer(s2, 70)  # 250 -> 180; 260 -> 330

    print(bank.summary())
    print("\n[Mini-Project 2] Fleet Management smoke test...")
    # TODO: create a Fleet, add Car/ElectricCar/Truck, display_all, filter_by_brand
    print("\n[Mini-Project 2] Fleet Management smoke test...")
    fleet = Fleet("GT Logistics")

    v1 = Car("Toyota", "Camry")
    v2 = ElectricCar("Tesla", "Model 3", battery_kwh=75)
    v3 = Truck("Ford", "F-150")

    fleet.add_vehicle(v1)
    fleet.add_vehicle(v2)
    fleet.add_vehicle(v3)

    # Show all vehicles (polymorphic show_details)
    print(fleet.display_all())

    # Filter by brand
    teslas = fleet.filter_by_brand("Tesla")
    print("\nFiltered by brand = Tesla:")
    for v in teslas:
        print(v.show_details())
    print("\n[Mini-Project 3] Student Grade System smoke test...")
    # TODO: create Student, add Grade objects, print transcript & GPA
    s = Student("Santosh")
    s.add_grade(Grade("Math", 90))
    s.add_grade(Grade("Science", 80))
    print("GPA:", s.gpa())

    s = Student("Santosh")
    s.add_grade(Grade("Math", 90))
    s.add_grade(Grade("Science", 80))
    s.add_grade(Grade("English", 95))
    print(s.display_transcript())