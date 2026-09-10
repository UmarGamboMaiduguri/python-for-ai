# Scatter Plot with Matplotlib
# Author: Umar Gambo

import matplotlib.pyplot as plt

math_scores = [55, 60, 65, 70, 75, 80, 85, 90]
computer_scores = [58, 63, 68, 72, 78, 82, 88, 95]

plt.scatter(math_scores, computer_scores)

plt.title("Math Scores vs Computer Science Scores")
plt.xlabel("Math Score")
plt.ylabel("Computer Science Score")

plt.xlim(0, 100)
plt.ylim(0, 100)

plt.tight_layout()
plt.show()
