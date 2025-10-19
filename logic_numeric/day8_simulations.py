# Day 8 – Simulation Problems (Traffic Lights, Pedestrian Crossing, and ATM)
# Purpose: Practice state-based logic using loops and conditionals.

# --- Traffic Light Sequence ---
lights = ["Green", "Yellow", "Red"]
cycles = 3

print("🚦 Traffic light sequence begins")
for cycle in range(cycles):
    for color in lights:
        print(f"Cycle {cycle + 1} - Light is {color}")
print("Sequence complete.\n")

# --- Pedestrian Crossing Simulation ---
lights = ["Green", "Red"]
cycles = 5

print("🚶 Pedestrian Crossing Simulation")
for cycle in range(cycles):
    for color in lights:
        print(f"Cycle {cycle + 1} - Light is {color}")
        if color == "Red":
            print("Pedestrian can Walk")
        else:
            print("DONT WALK")
print("Simulation complete.\n")

# --- (Optional) ATM Simulation for State Updates ---
balance = 1000
print("🏦 ATM Simulation (enter 0 to exit)")
while True:
    print(f"Current balance: ${balance}")
    amount = int(input("Enter amount to withdraw (0 to exit): "))
    if amount == 0:
        print("Transaction ended.")
        break
    elif amount > balance:
        print("❌ Insufficient funds.")
    elif amount % 10 != 0:
        print("❌ Please enter multiples of 10.")
    else:
        balance -= amount
        print(f"✅ Withdrawn ${amount}. Remaining balance: ${balance}\n")