

import numpy as np

def cntnz(M):
    n, m = M.shape
    
    cnt = 0

    for i in range(n):
        for j in range(m):
            if M[i][j] != 0:
                cnt += 1

    return cnt

def issymm(M):
    w, h = M.shape

    if w != h:
        return False
    
    return np.array_equal(M, M.T)

A = np.loadtxt('matrixA.csv', delimiter=',', dtype=int)
B = np.loadtxt('matrixB.csv', delimiter=',', dtype=int)
C = np.loadtxt('matrixC.csv', delimiter=',', dtype=int)

print('Aの非ゼロ要素数:', cntnz(A))
print('Bの非ゼロ要素数:', cntnz(B))
print('Cの非ゼロ要素数:', cntnz(C))

print('Aは' + ('対称行列' if issymm(A) else '非対称行列'))
print('Bは' + ('対称行列' if issymm(B) else '非対称行列'))
print('Cは' + ('対称行列' if issymm(C) else '非対称行列'))