groceries = {'apples': 5, 'bananas': 4, 'milk': 2, 'eggs': 3, 'bread': 1}

for item, qty in groceries.items():
    print(f"{item}: {qty}")
    if qty <= 3:
        choice = input(f"{item} is low on stock. Restock? (Y/N): ").strip().upper()
        if choice == 'Y':
            try:
                add = int(input(f"How many units of {item} to add? "))
                groceries[item] += add
                print(f"{item} updated → {groceries[item]}")
            except ValueError:
                print("Invalid number. Skipping.")

print("\nUpdated inventory:")
for item, qty in groceries.items():
    print(f"{item}: {qty}")

remaining_low = {i: q for i, q in groceries.items() if q <= 3}
if remaining_low:
    print("\nStill low:", remaining_low)
else:
    print("\nAll items are well stocked!")
