# Pandas Data Filtering Practice
# Author: Umar Gambo

import pandas as pd

data = {
    "name": ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"],
    "math": [85, 72, 65, 55, 90],
    "english": [78, 81, 70, 60, 88],
    "computer_science": [92, 75, 68, 58, 95]
}

students = pd.DataFrame(data)

print("--- Student Dataset ---")
print(students)

# Students with Math score above 70
high_math = students[students["math"] > 70]

print("\n--- Students with Math Score Above 70 ---")
print(high_math)

# Students with Computer Science score above 80
high_cs = students[students["computer_science"] > 80]

print("\n--- Students with Computer Science Score Above 80 ---")
print(high_cs)

# Find the highest Math score
highest_math = students["math"].max()

print("\n--- Highest Math Score ---")
print(highest_math)
