# NumPy Matrices Practice
# Author: Umar Gambo

import numpy as np

matrix = np.array([
    [80, 75, 90],
    [65, 70, 68],
    [92, 88, 95]
])

print("--- Student Score Matrix ---")
print(matrix)

print("\n--- Matrix Shape ---")
print(matrix.shape)

print("\n--- Column Averages ---")
print(np.mean(matrix, axis=0))

print("\n--- Row Averages ---")
print(np.mean(matrix, axis=1))

print("\n--- Transposed Matrix ---")
print(matrix.T)
