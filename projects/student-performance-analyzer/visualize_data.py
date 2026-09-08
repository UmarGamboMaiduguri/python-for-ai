# Student Performance Data Visualization
# Author: Umar Gambo

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data/sample_students.csv")

# Calculate average score for each subject
subjects = ["math", "english", "computer_science"]
averages = data[subjects].mean()

# Create a bar chart
averages.plot(kind="bar")

plt.title("Average Student Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.ylim(0, 100)

plt.tight_layout()
plt.show()
