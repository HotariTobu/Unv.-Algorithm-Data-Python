import math
from operator import itemgetter

text = input()

palindromes = []

for i, c in enumerate(text):
    if c not in 'ab':
        continue;

    f = i + 1

    while True:
        l = text.find(c, f)
        if l == -1:
            break

        is_palindrome = True

        for j in range(1, math.ceil((l - i) / 2)):
            if text[i + j] != text[l - j]:
                is_palindrome = False
                break

        if is_palindrome:
            # palindromes.append(text[i:l + 1])
            palindromes.append((i, l + 1))

        f = l + 1

# print(palindromes)

P = []

if len(palindromes) > 0:
    palindromes.sort(key=itemgetter(1))
    
    t = min(palindromes, key=itemgetter(0))[0]
    
    for palindrome in palindromes:
        if t <= palindrome[0]:
            P.append(palindrome)
            t = palindrome[1]

print(len(P))