# Pandas Data Cleaning Practice
# Author: Umar Gambo

import pandas as pd

# Create a dataset with missing values
data = {
    "name": ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"],
    "math": [85, 72, None, 55, 90],
    "english": [78, 81, 70, None, 88],
    "computer_science": [92, 75, 68, 58, 95]
}

students = pd.DataFrame(data)

print("--- Original Dataset ---")
print(students)

print("\n--- Missing Values ---")
print(students.isnull().sum())

# Fill missing scores with the column average
students["math"] = students["math"].fillna(students["math"].mean())
students["english"] = students["english"].fillna(students["english"].mean())

print("\n--- Cleaned Dataset ---")
print(students)

print("\n--- Missing Values After Cleaning ---")
print(students.isnull().sum())
