# Exploratory Data Analysis - Correlation Analysis
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

# Calculate correlations between subjects
correlation = students[subjects].corr()

print("--- Correlation Matrix ---")
print(correlation)

print("\n--- Interpretation ---")
print("A correlation close to 1 indicates a strong positive relationship.")
print("A correlation close to 0 indicates a weak linear relationship.")
print("A correlation close to -1 indicates a strong negative relationship.")
