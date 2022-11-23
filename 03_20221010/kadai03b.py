import random

s = int(input())

random.seed(s)

nums = [random.randint(1, 1000) for _ in range(100)]

print(nums)
print('max:', max(nums))
print('min:', min(nums))