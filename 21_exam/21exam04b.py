import numpy as np
from numpy.linalg import det

path = input()

A = np.loadtxt(path, int, delimiter=',')
n = A.shape[0]
b = np.ones(n)

x = np.empty(n)

detA = det(A)
for i in range(n):
    B = A.copy()
    # for j in range(n):
    #     B[j, i] = 1
    B[:, i] = b

    x[i] = det(B) / detA

cx = np.linalg.solve(A, b)

print(np.allclose(x, cx))