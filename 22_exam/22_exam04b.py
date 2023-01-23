import numpy as np

V = [int(token) for token in input().split()]
n = len(V)

A = []
for i in range(n, 0, -1):
    r = V[i:] + V[:i]
    A.append(r)

npA = np.array(A, int)

print(npA)
print(np.linalg.det(npA))