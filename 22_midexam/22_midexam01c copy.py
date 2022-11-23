n, m = [int(token) for token in input().split()]
s, t = [int(token) for token in input().split()]

lines = [input().split() for _ in range(m)]
E = [list(map(int, line)) for line in lines]

L = [list() for _ in range(n)]
for e in E:
    i0 = e[0]
    i1 = e[1]

    L[i0].append(i1)
    L[i1].append(i0)

def isconnected(s: int, t: int, l: list = list()) -> bool:
    for v in L[s]:
        if v in l:
            continue

        l.append(v)

        if v == t or isconnected(v, t, l):
            return True
    
    return False

if isconnected(s, t):
    print('Yes')
else:
    print('No')