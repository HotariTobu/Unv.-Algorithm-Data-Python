import math
import random
import time

s = int(input())
a = int(input())
n = int(input())
x = int(input())

random.seed(s)

A = [random.randint(1, a) for _ in range(n)]

A.sort()

def measure(f):
    start = time.time()
    result = f()
    end = time.time()
    return (result, end - start)

def contains1():
    return x in A

def contains2():
    for y in A:
        if x == y:
            return True
    
    return False

def contains3():
    left = 0
    right = len(A)

    while left + 1 < right:
        center = math.floor((left + right) / 2)
        if x < A[center]:
            right = center
        else:
            left = center

    return A[left] == x

funcs = [contains1, contains2, contains3]

for i, func in enumerate(funcs):
    result, measured_time = measure(func)
    print(f"手法{i + 1}:", x, 'を発見' if result else 'は存在しません', '実行時間', measured_time)