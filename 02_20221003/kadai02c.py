price = int(input())

count = 0
fee = 0

while True:
    age = int(input())
    if age == -1:
        break

    count += 1

    if age < 13:
        fee += int(price * 0.5)
    elif age < 60:
        fee += price
    else:
        fee += int(price * 0.8)

if count >= 5:
    fee = int(fee * 0.9)

print(fee)