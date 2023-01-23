W = [0] + [int(token) for token in input().split()]
L, p, q = [int(token) for token in input().split()]
n = len(W) - 1

def l(j, i):
    return i - j + sum(W[j:i + 1])

def pe(j, i):
    l_ji = l(j, i)

    if l_ji <= L - 5:
        return p
    else:
        return max(0, q * (l_ji - L))

OPT = [0]

for i in range(1, n + 1):
    min_p = min(OPT[j] + pe(j + 1, i) for j in range(i))
    OPT.append(min_p)

print(OPT[n])