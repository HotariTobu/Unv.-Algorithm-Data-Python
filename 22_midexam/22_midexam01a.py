# def n16ton10(c: str) -> int:
#     if c == 'a':
#         return 10
#     if c == 'b':
#         return 11
#     if c == 'c':
#         return 12
#     if c == 'd':
#         return 13
#     if c == 'e':
#         return 14
#     if c == 'f':
#         return 15
#     return int(c)

# n16 = input()

# factor = 1
# n10 = 0

# for c in n16[::-1]:
#     n10 += n16ton10(c) * factor
#     factor *= 16

# print(n10)

print(int(input(), base=16))