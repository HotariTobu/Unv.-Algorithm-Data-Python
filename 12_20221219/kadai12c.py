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
        
print(OPT[n][k])
