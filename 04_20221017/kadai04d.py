import math
from pyclbr import Function

P = [int(s) for s in input().split()]
N = [int(s) for s in input().split()]
B = int(input())

def f(A):
    sum = 0
    for p, n in zip(P, N):
        sum += min(A * n, 1000 - p)
    return sum

def find(target: int, left: int, right: int, f: Function):
    while left + 1 < right:
        center = math.floor((left + right) / 2)
        if target < f(center):
            right = center
        else:
            left = center
    return left

# A = 0

# while B >= f(A + 1):
#     A += 1

left = B // sum(N)
right = B
A = find(B, left, right, f)

print(A)