from operator import itemgetter

n = int(input())
j = int(input())
lines = [input().split() for _ in range(n)]
tasks = [tuple([int(s), int(f), int(v)]) for s, f, v in lines]

tasks.sort(key=itemgetter(1))

def find(t, l, r, f):
    while l + 1 < r:
        center = (l + r) // 2
        if t < f(center):
            r = center
        else:
            l = center
    return l

def q(j):
    qj = j - 2
    sj = tasks[j - 1][0]

    qj = find(sj, 0, qj, lambda i: tasks[i][1])

    return qj + 1

# def q(j):
#     qj = j - 2
#     sj = tasks[j - 1][0]

#     while qj >= 0 and tasks[qj][1] > sj:
#         qj -= 1

#     return qj + 1

print(q(j))