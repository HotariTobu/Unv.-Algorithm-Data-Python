k = int(input())
lines = [input().split() for _ in range(k)]
stas_list = [tuple(token == '1' for token in line) for line in lines]
n = len(stas_list[0])

OPT = [n] * n
OPT[0] = 0

for i in range(1, n):
    cands = [n]

    for stas in stas_list:
        if not stas[i]:
            continue
        
        j = i
        while j >= 0:
            j -= 1
            if stas[j]:
                break
            
        if j >= 0:
            cands.append(OPT[j] + 1)

    OPT[i] = min(cands)

print(OPT[-1])