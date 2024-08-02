import numpy as np

m = np.arange(1, 21).reshape(4, 5)
arr_zeros = np.zeros(10)
arr_ones = np.ones(10)
arr_fives = np.ones(10) * 5
arr_even_integers = np.arange(10, 51, 2)
rand_num = np.random.rand()
np.savetxt('matrix.txt', m)
loaded_m = np.loadtxt('matrix.txt')

print("i. 4 x 5 matrix with values ranging from 1 to 20:")
print(m)
print("\nii. Array of 10 zeros:")
print(arr_zeros)
print("\nArray of 10 ones:")
print(arr_ones)
print("\nArray of 10 fives:")
print(arr_fives)
print("\niii. Array of even integers from 10 to 50:")
print(arr_even_integers)
print("\niv. Random number between 0 and 1:")
print(rand_num)
print("\nv. Loaded matrix from file:")
print(loaded_m)
