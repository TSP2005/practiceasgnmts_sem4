import numpy as np
import time

a = np.random.rand(106, 104)
b = np.random.rand(104, 106)

def mat_mult(X, Y):
    return np.dot(X, Y)

start_time = time.time()
result_loops = np.zeros((a.shape[0], b.shape[1]))
for i in range(a.shape[0]):
    for j in range(b.shape[1]):
        for k in range(b.shape[0]):
            result_loops[i, j] += a[i, k] * b[k, j]
end_time = time.time()
time_loops = end_time - start_time

start_time = time.time()
result_vectorized = mat_mult(a, b)
end_time = time.time()
time_vectorized = end_time - start_time

speedup = time_loops / time_vectorized

print("Loops Result:\n", result_loops)
print("\nVectorized Result:\n", result_vectorized)
print("\nTime using loops:", time_loops, "seconds")
print("Time using vectorization:", time_vectorized, "seconds")
print("Speedup:", speedup)

