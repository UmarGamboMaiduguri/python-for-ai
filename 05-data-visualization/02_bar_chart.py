# Bar Chart with Matplotlib
# Author: Umar Gambo

import matplotlib.pyplot as plt

students = ["Aisha", "Ibrahim", "Fatima", "Musa", "Zainab"]
scores = [85, 72, 65, 55, 90]

plt.bar(students, scores)

plt.title("Student Scores by Name")
plt.xlabel("Students")
plt.ylabel("Score")

plt.ylim(0, 100)

plt.tight_layout()
plt.show()
