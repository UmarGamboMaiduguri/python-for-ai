# NumPy Operations Practice
# Author: Umar Gambo

import numpy as np

scores = np.array([60, 70, 80, 90, 100])

print("--- Original Scores ---")
print(scores)

print("\n--- Add 5 Points ---")
print(scores + 5)

print("\n--- Double the Scores ---")
print(scores * 2)

print("\n--- Scores Above 75 ---")
print(scores[scores > 75])

print("\n--- Average ---")
print(np.mean(scores))
