

import numpy as np

n, s = [int(token) for token in input().split()]

In = np.identity(n, int)

def jcbslv(A, b, x = np.zeros(n)):
    cnt += 1

    if cnt > 100 or np.linalg.norm(np.dot(A, x) - b) <= 1e-6:
        return x

    D = A * In
    N = A - D

    Di = In / D

    # x0 = jcbslv()



np.random.seed(s)

A = np.random.randint(0, 2, (n, n))
A += In * n

b = np.random.randint(0, 2 * n, n)

D = A * In
N = A - D

Di = In.copy()
for i in range(n):
    Di[i][i] /= D[i][i]

x = np.zeros(n)

for i in range(100):
    x = np.dot(Di, np.dot(-N, x) + b)
    if np.linalg.norm(np.dot(A, x) - b) <= 1e-6:
        cnt = i + 1
        break

cx = np.linalg.solve(A, b)

print(np.allclose(x, cx))