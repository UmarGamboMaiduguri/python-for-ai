# Python Dictionaries Practice
# Author: Umar Gambo

student = {
    "name": "Aisha",
    "age": 22,
    "math": 85,
    "english": 78,
    "computer_science": 92
}

print("--- Student Information ---")

print("Name:", student["name"])
print("Age:", student["age"])
print("Math:", student["math"])
print("English:", student["english"])
print("Computer Science:", student["computer_science"])

average = (
    student["math"]
    + student["english"]
    + student["computer_science"]
) / 3

print("Average:", round(average, 2))

print("\n--- All Student Data ---")

for key, value in student.items():
    print(key, ":", value)
