import math

x = int(input())
A = [int(s) for s in input().split()]

A.sort()

left = 0
right = len(A)

while left + 1 < right:
    center = math.floor((left + right) / 2)
    print(left, center, right)
    if x < A[center]:
        right = center
    else:
        left = center

if A[left] == x:
    print('yes')
else:
    print('no')