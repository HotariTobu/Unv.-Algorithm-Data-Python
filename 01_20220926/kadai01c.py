from cmath import sqrt


x = int(input())

d = None
for i in range(2, x):
    if x % i == 0:
        d = i

if d is None:
    print("prime")
else:
    print(d)