d = [int(token) for token in input().split()]
n = len(d) - 1

OPT = [[0] * n for _ in range(n)]

for i in range(1, n):
    for s in range(n - i):
        vs = [OPT[s][k] + OPT[k + 1][s + i] + d[s] * d[k + 1] * d[s + i + 1] for k in range(s, s + i)]
        OPT[s][s + i] = min(vs)

def chunk(s, t):
    def concat(s, t):
        result = ''
        for i in range(s + 1, t + 2):
            result += 'A' + str(i)
        return result

    if s == t or s == t - 1:
        return concat(s, t)

    for k in range(s, t):
        if OPT[s][t] == OPT[s][k] + OPT[k + 1][t] + d[s] * d[k + 1] * d[t + 1]:
            min_k = k
            break

    L = chunk(s, min_k)
    R = chunk(min_k + 1, t)

    if s == k:
        return f"{L}({R})"
    elif k + 1 == t:
        return f"({L}){R}"
    else:
        return f"({L})({R})"

print(chunk(0, n - 1))