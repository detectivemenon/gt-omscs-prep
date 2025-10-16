start_number = int(input("Enter a starting number: "))
end_number = int(input("Enter the ending number: "))

even_count = 0
odd_count = 0
for n in range(start_number, end_number + 1):
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"There are {even_count} even numbers and {odd_count} odd numbers.") 
