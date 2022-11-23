x = int(input())
y = int(input())

a = x

for n in range(y):
    a = (2 * a + x / (a * a)) / 3

print(a)
print(a ** 3)