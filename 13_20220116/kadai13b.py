d = [int(token) for token in input().split()]
n = len(d) - 1

OPT = [[0] * n for _ in range(n)]

for i in range(1, n):
    for s in range(n - i):
        vs = [OPT[s][k] + OPT[k + 1][s + i] + d[s] * d[k + 1] * d[s + i + 1] for k in range(s, s + i)]
        OPT[s][s + i] = min(vs)

print(OPT[0][n - 1])