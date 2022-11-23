n, m = [int(token) for token in input().split()]
s, t = [int(token) for token in input().split()]

lines = [input().split() for _ in range(m)]
E = [list(map(int, line)) for line in lines]

L = [False] * n
L[s] = True

for _ in range(n - 1):
    for e in E:
        i0 = e[0]
        i1 = e[1]

        if L[i0]:
            L[i1] = True
        elif L[i1]:
            L[i0] = True

if L[t]:
    print('Yes')
else:
    print('No')