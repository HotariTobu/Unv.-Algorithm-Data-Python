W = [int(token) for token in input().split()]
L, p, q = [int(token) for token in input().split()]
n = len(W)

ps_list = []

for j in range(n):
    ps = []

    l_s = -1
    l_w = 0
    
    for i in range(j, n):
        l_s += 1
        l_w += W[i]

        l = l_s + l_w

        if l <= L - 5:
            pe = p
        else:
            pe = max(0, q * (l - L))
        
        ps.append(pe)

    ps_list.append(ps)

OPT = []

for i in range(n):
    min_p = min([ps_list[0][i]] + [OPT[j - 1] + ps_list[j][i] for j in range(1, i)])
    OPT.append(min_p)

print(OPT[n])