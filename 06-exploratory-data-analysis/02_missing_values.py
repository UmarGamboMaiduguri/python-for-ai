# Exploratory Data Analysis - Missing Values
# Author: Umar Gambo

import pandas as pd

# Create a dataset with missing values
data = {
    "name": ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"],
    "math": [85, 72, None, 55, 90],
    "english": [78, None, 70, 60, 88],
    "computer_science": [92, 75, 68, None, 95]
}

students = pd.DataFrame(data)

print("--- Original Dataset ---")
print(students)

print("\n--- Missing Values ---")
print(students.isnull().sum())

print("\n--- Total Missing Values ---")
print(students.isnull().sum().sum())

# Fill missing numerical values with column averages
students["math"] = students["math"].fillna(students["math"].mean())
students["english"] = students["english"].fillna(students["english"].mean())
students["computer_science"] = students["computer_science"].fillna(
    students["computer_science"].mean()
)

print("\n--- Cleaned Dataset ---")
print(students)

print("\n--- Missing Values After Cleaning ---")
print(students.isnull().sum())
