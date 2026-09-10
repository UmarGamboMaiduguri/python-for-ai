# Exploratory Data Analysis - Descriptive Statistics
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

subjects = ["math", "english", "computer_science"]

print("--- Descriptive Statistics ---")

print("\nMean:")
print(students[subjects].mean())

print("\nMedian:")
print(students[subjects].median())

print("\nMinimum:")
print(students[subjects].min())

print("\nMaximum:")
print(students[subjects].max())

print("\nStandard Deviation:")
print(students[subjects].std())

print("\n--- Complete Summary ---")
print(students[subjects].describe())
