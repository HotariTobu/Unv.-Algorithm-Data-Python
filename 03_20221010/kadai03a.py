from cmath import sqrt


a = int(input())
b = int(input())
c = int(input())

d = b * b - 4 * a * c
e = 2 * a

if d < 0:
    print('no solution')
elif d > 0:
    f = -b
    g = sqrt(d).real
    print((f + g) / e, (f - g) / e)
else:
    print(-b / e)