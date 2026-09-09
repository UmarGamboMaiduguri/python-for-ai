# Searching and Sorting Algorithms
# Author: Umar Gambo

numbers = [42, 15, 8, 23, 4, 16, 9]

print("--- Original List ---")
print(numbers)

# Linear Search
target = 23
found = False

for number in numbers:
    if number == target:
        found = True
        break

print("\n--- Linear Search ---")
print("Target:", target)
print("Found:", found)

# Bubble Sort
sorted_numbers = numbers.copy()

for i in range(len(sorted_numbers)):
    for j in range(0, len(sorted_numbers) - i - 1):
        if sorted_numbers[j] > sorted_numbers[j + 1]:
            sorted_numbers[j], sorted_numbers[j + 1] = (
                sorted_numbers[j + 1],
                sorted_numbers[j]
            )

print("\n--- Bubble Sort ---")
print("Sorted list:", sorted_numbers)
