import math

def f(x):
    return math.exp(x) + 7 * x ** 3

a = float(input())

threshold = 1e-5

left = 0
right = 1

while right - left > threshold:
    center = (left + right) / 2
    if a < f(center):
        right = center
    else:
        left = center

x = left

print(x)
print(f(x))