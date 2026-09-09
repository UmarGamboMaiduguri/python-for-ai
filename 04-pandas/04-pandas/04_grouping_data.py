# Pandas Grouping Data Practice
# Author: Umar Gambo

import pandas as pd

data = {
    "name": ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"],
    "department": ["CS", "CS", "IT", "IT", "CS"],
    "score": [85, 72, 65, 55, 90]
}

students = pd.DataFrame(data)

print("--- Student Dataset ---")
print(students)

# Calculate average score by department
department_average = students.groupby("department")["score"].mean()

print("\n--- Average Score by Department ---")
print(department_average)

# Find the highest score in each department
department_highest = students.groupby("department")["score"].max()

print("\n--- Highest Score by Department ---")
print(department_highest)
