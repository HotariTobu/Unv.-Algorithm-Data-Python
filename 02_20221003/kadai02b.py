a = int(input())
b = int(input())

result = ''

while a > 0:
    result = str(a % b) + result
    a //= b

if result == '':
    result = 0

print(result)