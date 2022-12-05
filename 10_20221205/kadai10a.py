

import numpy as np

np.random.seed(1)

n = int(input('input n: '))

A = np.random.randint(5, 10, (n, n))
print('A =\n', A)

B = np.empty((n, n), int)
for i in range(n):
    for j in range(n):
        B[i][j] = (i + j) % 10
print('B =\n', B)

C = A + B
print('C =\n', C)