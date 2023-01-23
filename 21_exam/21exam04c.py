A = [int(token) for token in input().split()]

def f(A):
    n = len(A)

    if n == 1:
        PA = sA = tA = max(0, A[0])
        qA = A[0]
    else:
        i = n // 2
        B = A[:i]
        C = A[i:]

        PB, qB, sB, tB = f(B)
        PC, qC, sC, tC = f(C)

        PA = max(PB, PC, tB + sC)
        qA = qB + qC
        sA = max(sB, qB + sC)
        tA = max(tC, tB + qC)

    return PA, qA, sA, tA

print(f(A)[0])