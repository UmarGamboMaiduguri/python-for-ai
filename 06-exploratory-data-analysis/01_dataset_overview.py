# Exploratory Data Analysis - Dataset Overview
# Author: Umar Gambo

import pandas as pd

# Create a sample dataset
data = {
    "name": ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"],
    "math": [85, 72, 65, 55, 90],
    "english": [78, 81, 70, 60, 88],
    "computer_science": [92, 75, 68, 58, 95]
}

students = pd.DataFrame(data)

print("--- Dataset ---")
print(students)

print("\n--- Dataset Shape ---")
print("Rows:", students.shape[0])
print("Columns:", students.shape[1])

print("\n--- Column Names ---")
print(students.columns.tolist())

print("\n--- Data Types ---")
print(students.dtypes)

print("\n--- Basic Statistics ---")
print(students.describe())

print("\n--- Missing Values ---")
print(students.isnull().sum())
