import numpy as np

matrix = np.random.randint(0, 10, (5, 6))

flat_matrix = matrix.flatten()
unique_values, counts = np.unique(flat_matrix, return_counts=True)
frequency_dict = dict(zip(unique_values, counts))
for val, freq in frequency_dict.items():
print(f"Value {val} appears {freq} times.")
