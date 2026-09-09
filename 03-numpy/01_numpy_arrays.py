# NumPy Arrays Practice
# Author: Umar Gambo

import numpy as np

# Create a NumPy array
scores = np.array([85, 72, 65, 90, 78])

print("--- Student Scores ---")
print(scores)

print("\n--- Array Information ---")
print("Shape:", scores.shape)
print("Size:", scores.size)
print("Data type:", scores.dtype)

print("\n--- Basic Statistics ---")
print("Total:", np.sum(scores))
print("Average:", np.mean(scores))
print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))
