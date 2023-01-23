n = int(input())
m = int(input())
lines = [input().split() for _ in range(m)]
E = {(int(u), int(v)): int(l) for u, v, l in lines}

s = 0
t = n - 1

inf = sum(E.values())

L = [inf] * n
L[s] = 0

for _ in range(n - 1):
    for (u, v), l in E.items():
        Lul = L[u] + l
        if L[v] > Lul:
            L[v] = Lul

print(L[t])