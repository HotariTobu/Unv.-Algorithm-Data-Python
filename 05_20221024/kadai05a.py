amount = int(input())

bills = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]

count = 0

for bill in bills:
    count += amount // bill
    amount = amount % bill

print(count)