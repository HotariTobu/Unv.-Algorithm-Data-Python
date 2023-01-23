vs = [int(token) for token in input().split()]

cnts = {}

for v in vs:
    if v in cnts:
        cnts[v] += 1
    else:
        cnts[v] = 1

re = [v for v, cnt in cnts.items() if cnt == 1]
re.sort()
print(*re)