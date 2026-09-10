# Line Chart with Matplotlib
# Author: Umar Gambo

import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
scores = [60, 68, 72, 80, 88]

plt.plot(months, scores, marker="o")

plt.title("Student Performance Progress")
plt.xlabel("Month")
plt.ylabel("Score")

plt.ylim(0, 100)

plt.tight_layout()
plt.show()
