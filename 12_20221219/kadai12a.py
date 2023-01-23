W = int(input())
w = [int(token) for token in input().split()]
v = [int(token) for token in input().split()]

n = len(w)

w.insert(0, -1)
v.insert(0, -1)

OPT = [[0] * (W + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    wi = w[i]
    vi = v[i]

    for j in range(1, W + 1):
        if j < wi:
            OPT[i][j] = OPT[i - 1][j]
        else:
            OPT[i][j] = max(OPT[i - 1][j], vi + OPT[i - 1][j - wi])

print(OPT[n][W])