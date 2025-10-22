"""
Day 16 – OOP Part 2: Clean Design & Pythonic Tools
Sections:
  1) Composition vs Inheritance (Engine + Car)
  2) Properties (Pythonic getters/setters)
  3) Dunder methods (__str__, __repr__, __eq__, optional __lt__)
  4) Dataclasses (record-like classes with less boilerplate)
  5) Mini-Challenge: Garage 2.0 (composition + queries)
"""

from dataclasses import dataclass  # Used in Section 4
from typing import List, Optional


# ---------------------------------------------------------------------
# 1) Composition vs Inheritance
# ---------------------------------------------------------------------
class Engine:
    """
    Represents an engine used BY a Car (composition).
    """
    def __init__(self, hp: int, motor_type: str):
        # TODO: store hp (horsepower) and motor_type (e.g., "ICE", "EV", "Hybrid")
        self.hp = hp
        self.motor_type = motor_type


    def specs(self) -> str:
        # TODO: return a human-friendly string describing this engine
        return f"{self.hp} HP {self.motor_type}"



class Car:
    """
    A Car that HAS an Engine (composition).
    """
    wheels = 4  # class variable shared by all cars

    def __init__(self, brand: str, model: str, year: int, engine: Engine):
        # TODO: set instance attributes; store the Engine instance
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine  # Composition → this Car “has an” Engine


    def show_details(self) -> None:
        # TODO: print details including engine specs
        print(f"{self.year} {self.brand} {self.model} | Engine: {self.engine.specs()}")

# ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        # Reuse the Car constructor for brand/model/year
        super().__init__(brand, model, year, engine=None)
        self.battery_size = battery_size

    def show_details(self):
        # Override the base class method
        print(f"{self.year} {self.brand} {self.model} | Battery: {self.battery_size} kWh")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # notice the double underscore (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance = ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance = ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def show_balance(self):
        print(f"Current balance for {self.owner}: ${self.__balance}")

# ---------------------------------------------------------------------
# 2) Properties (validation without clunky get_/set_ methods)
# ---------------------------------------------------------------------
class TripCounter:
    """
    Example for @property: keep total_miles non-negative,
    and allow resetting the trip counter.
    """
    def __init__(self, total_miles: int = 0):
        # TODO: assign to the backing attribute (e.g., _total_miles)
        pass

    @property
    def total_miles(self) -> int:
        # TODO: return the backing attribute
        pass

    @total_miles.setter
    def total_miles(self, value: int) -> None:
        # TODO: validate non-negative; raise ValueError otherwise
        pass

    def reset_trip(self) -> None:
        # TODO: add a simple trip counter and reset it here (optional)
        pass


# ---------------------------------------------------------------------
# 3) Dunder Methods: __str__, __repr__, __eq__ (optional __lt__)
# ---------------------------------------------------------------------
class Vehicle:
    """
    Base for demonstrating dunders; Car could also inherit from this if you like,
    but we’ll keep it separate to focus on the dunders themselves.
    """
    def __init__(self, vin: str, brand: str, model: str, year: int):
        self.vin = vin
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        # TODO: human-readable string (for print)
        # e.g., "2024 Tesla Model 3 (VIN: ABC123)"
        pass

    def __repr__(self) -> str:
        # TODO: unambiguous/debug-friendly representation
        # e.g., "Vehicle(vin='ABC123', brand='Tesla', model='Model 3', year=2024)"
        pass

    def __eq__(self, other: object) -> bool:
        # TODO: equality by VIN (if other is a Vehicle)
        # Return NotImplemented if other is not a Vehicle
        pass

    # Optional (enable sorting by year, oldest first)
    # def __lt__(self, other: "Vehicle") -> bool:
    #     return self.year < other.year


# ---------------------------------------------------------------------
# 4) Dataclass Example (record-like class)
# ---------------------------------------------------------------------
@dataclass(frozen=False)
class ServiceRecord:
    """
    A lightweight record of a service event.
    Dataclass auto-generates __init__, __repr__, __eq__, etc.
    """
    date: str
    description: str
    cost: float = 0.0


# ---------------------------------------------------------------------
# 5) Mini-Challenge – Garage 2.0 (composition + queries)
# ---------------------------------------------------------------------
class Garage:
    """
    A Garage that stores Vehicles (composition).
    Features:
      - add_car(vehicle): prevent duplicates (by VIN)
      - find_by_brand(brand) -> List[Vehicle]
      - oldest() -> Optional[Vehicle]
      - nice __str__ that lists inventory
    """
    def __init__(self, name: str):
        self.name = name
        self._inventory: List[Vehicle] = []
        self._vin_index = set()  # to prevent duplicate VINs

    def add_car(self, vehicle: Vehicle) -> bool:
        # TODO:
        #  - if vehicle.vin already in _vin_index, return False
        #  - else, add to _inventory and _vin_index, return True
        pass

    def find_by_brand(self, brand: str) -> List[Vehicle]:
        # TODO: filter vehicles matching brand (case-insensitive recommended)
        pass

    def oldest(self) -> Optional[Vehicle]:
        # TODO: return min by year or None if empty
        pass

    def __str__(self) -> str:
        # TODO: pretty-print: f"Garage: {self.name}\n" + list all vehicles one per line
        pass


# ---------------------------------------------------------------------
# Demo / Scratch Area
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # --- Section 1 demo ---
    # TODO: create an Engine and a Car that uses it; call show_details()
    eng = Engine(200, "ICE")
    car = Car("Toyota", "Camry", 2021, eng)
    car.show_details()
    tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
    tesla.show_details()

    # --- Demonstrating Polymorphism ---
    eng1 = Engine(250, "ICE")
    eng2 = Engine(0, "EV")  # EV still reuses Engine structure for illustration

    toyota = Car("Toyota", "Camry", 2022, eng1)
    tesla = ElectricCar("Tesla", "Model Y", 2024, 82)

    garage = [toyota, tesla]

    for vehicle in garage:
        vehicle.show_details()  # same method call, different behaviors

    acct1 = BankAccount("Santosh", 1000)
    acct1.show_balance()

    acct1.deposit(500)
    acct1.withdraw(300)

    # Try to directly modify the balance
    acct1.__balance = 999999
    acct1.show_balance()  # still shows the protected real balance!
    # --- Section 2 demo ---
    # TODO: create TripCounter and try setting/reading total_miles (including invalid)
    # trip = TripCounter(total_miles=100)
    # trip.total_miles = 150
    # print(trip.total_miles)

    # --- Section 3 demo ---
    # TODO: create a couple Vehicles, print(str/ repr), compare equality, optionally sort
    # v1 = Vehicle(vin="VIN123", brand="Tesla", model="Model 3", year=2024)
    # v2 = Vehicle(vin="VIN999", brand="Toyota", model="Camry", year=2019)
    # print(v1)
    # print(repr(v1))
    # print(v1 == v2)

    # --- Section 4 demo ---
    # TODO: create a ServiceRecord and print it
    # rec = ServiceRecord(date="2025-10-21", description="Oil change", cost=79.0)
    # print(rec)

    # --- Section 5 demo ---
    # TODO: create a Garage, add several Vehicles, find_by_brand, print oldest, print garage
    # g = Garage("Downtown Garage")
    # g.add_car(v1)
    # g.add_car(v2)
    # print(g.find_by_brand("tesla"))
    # print("Oldest:", g.oldest())
    # print(g)
    pass