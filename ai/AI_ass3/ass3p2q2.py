import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

sc = arr[:, 1]
lr = arr[-1, :]

print("Second Column:", sc)
print("Last Row:", lr)
