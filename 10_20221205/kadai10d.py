

import numpy as np
from time import time

def measure(f):
    start = time()
    result = f()
    end = time()
    return result, end - start

def strdot(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B

    subA = []
    subB = []

    step = n // 2
    for r in range(2):
        rs = r * step
        re = rs + step
        for c in range(2):
            cs = c * step
            ce = cs + step
            subA.append(A[rs:re, cs:ce])
            subB.append(B[rs:re, cs:ce])

    A11, A12, A21, A22 = subA
    B11, B12, B21, B22 = subB

    P1 = strdot(A11, B12 - B22)
    P2 = strdot(A11 + A12, B22)
    P3 = strdot(A21 + A22, B11)
    P4 = strdot(A22, B21 - B11)
    P5 = strdot(A11 + A22, B11 + B22)
    P6 = strdot(A12 - A22, B21 + B22)
    P7 = strdot(A11 - A21, B11 + B12)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P1 + P5 - P3 - P7

    C1 = np.concatenate([C11, C12], 1)
    C2 = np.concatenate([C21, C22], 1)

    C = np.concatenate([C1, C2], 0)
    return C

n, s = [int(token) for token in input().split()]

np.random.seed(s)

A = np.random.randint(0, 2, (n, n))
B = np.random.randint(0, 2, (n, n))

AB, strt = measure(lambda: strdot(A, B))
cAB = np.dot(A, B)

print('Strassen: time', strt, 'sec')
print(np.array_equal(AB, cAB))