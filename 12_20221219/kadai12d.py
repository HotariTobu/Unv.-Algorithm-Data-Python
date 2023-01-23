r = int(input())
k = int(input())
x = [int(token) for token in input().split()]

n = len(x)

x.insert(0, -1)

def p(i):
    for ip in range(1, i + 1):
        if x[ip] >= x[i] - r:
            return ip

OPT = [[0] * (k + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    pi = p(i)

    for j in range(1, k + 1):
        OPT[i][j] = max(OPT[i - 1][j], OPT[pi - 1][j - 1] + i - pi + 1)
       
i = n
j = k
X = []

while i > 0 and j > 0:
    if OPT[i][j] == OPT[i - 1][j]:
        i -= 1
    else:
        X.insert(0, x[i])
        i = p(i) - 1
        j -= 1

print(*X)