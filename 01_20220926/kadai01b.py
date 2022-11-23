a = int(input())
b = int(input())
c = int(input())

sum = 0
for i in range(a, b):
    if i % c == 0:
        sum += i

print(sum)