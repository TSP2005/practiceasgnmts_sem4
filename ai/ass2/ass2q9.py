import numpy as np

matrix = np.random.randint(0, 10, size=(8, 7))
max_vals = np.max(matrix, axis=0)
min_vals = np.min(matrix, axis=1)

print("Random Matrix:")
print(matrix)
print("Maximum values for each feature:")
print(max_vals)
print("Minimum values for each feature:")
print(min_vals)
