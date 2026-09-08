# Student Performance Data Analysis
# Author: Umar Gambo

import pandas as pd

# Load the dataset
data = pd.read_csv("data/sample_students.csv")

# Display the dataset
print("\n--- Student Dataset ---")
print(data)

# Calculate average scores
print("\n--- Average Scores ---")
print(data[["math", "english", "computer_science"]].mean())

# Calculate each student's average
data["average"] = data[["math", "english", "computer_science"]].mean(axis=1)

# Display student averages
print("\n--- Student Averages ---")
print(data[["name", "average"]])

# Find the highest-performing student
top_student = data.loc[data["average"].idxmax()]

print("\n--- Top Performing Student ---")
print(f"Name: {top_student['name']}")
print(f"Average: {top_student['average']:.2f}")
