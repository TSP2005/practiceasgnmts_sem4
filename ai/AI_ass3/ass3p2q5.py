import numpy as np

coefficient_matrix_A = np.random.rand(3, 3)
vector_b = np.random.rand(3, 1)
solution_vector_x = np.linalg.solve(coefficient_matrix_A, vector_b)

print("Coefficient Matrix A:")
print(coefficient_matrix_A)

print("\nVector b:")
print(vector_b)

print("\nSolution vector x:")
print(solution_vector_x)
