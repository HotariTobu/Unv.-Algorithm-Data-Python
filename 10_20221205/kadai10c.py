

import numpy as np
from time import time

def measure(f):
    start = time()
    result = f()
    end = time()
    return result, end - start

def jcbslv(A, b):
    n = b.size

    D = A * np.identity(n, int)
    N = A - D

    Di = np.zeros((n, n))
    for i in range(n):
        Di[i][i] = 1 / D[i][i]

    x = np.zeros(n)

    for i in range(100):
        x = np.dot(Di, np.dot(-N, x) + b)
        if np.linalg.norm(np.dot(A, x) - b) <= 1e-6:
            return x, i

    return x, 100

n, s = [int(token) for token in input().split()]

np.random.seed(s)

A = np.random.randint(0, 2, (n, n))
A += np.identity(n, int) * n

b = np.random.randint(0, 2 * n, n)

(x, cnt), jcbt = measure(lambda: jcbslv(A, b))
cx, nlst = measure(lambda: np.linalg.solve(A, b))

print('Jacobi: iteration', cnt, 'time', jcbt, 'sec')
print('np.linalg.solve: time', nlst, 'sec')
print(np.allclose(x, cx))