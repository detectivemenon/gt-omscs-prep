# Day 6 – Enumerate & Index Thinking (traditional Python)

nums = [10, 20, 30, 40, 50]

print("Index-based iteration:")
for i in range(len(nums)):
    print(f"Index {i} -> Value {nums[i]}")

print("\nEnumerate (index + value):")
for i, val in enumerate(nums):
    print(f"Index {i} -> Value {val}")

print("\nEvery 2nd element by index (0-based):")
for i, val in enumerate(nums):
    if i % 2 == 0:
        print(f"nums[{i}] = {val}")

print("\nManual reverse into a new list:")
reversed_list = []
for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])
print(reversed_list)

print("\nIn-place reverse using symmetric swaps:")
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n // 2):
    j = n - 1 - i
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
print(arr)