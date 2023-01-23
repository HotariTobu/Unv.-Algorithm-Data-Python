A = [int(token) for token in input().split()]

def isdegarr(A):
    A.sort()
    n = len(A)
    if A[-1] >= n or A[0] < 0:
        return False
    elif A[-1] == 0:
        return True

    i = n - 1 - A[-1]
    B = A[:i] + [a - 1 for a in A[i:-1]]

    return isdegarr(B)

print('yes' if isdegarr(A) else 'no')