# Basic Data Visualization with Matplotlib
# Author: Umar Gambo

import matplotlib.pyplot as plt

# Student scores
students = ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"]
scores = [85, 72, 65, 55, 90]

# Create a line plot
plt.plot(students, scores, marker="o")

# Add title and labels
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")

# Set score range
plt.ylim(0, 100)

# Display the plot
plt.tight_layout()
plt.show()
