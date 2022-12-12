from operator import itemgetter

n = int(input())
lines = [input().split() for _ in range(n)]
tasks = [tuple([int(s), int(f), int(v)]) for s, f, v in lines]

tasks.sort(key=itemgetter(1))

def q(j):
    qj = j - 2
    sj = tasks[j - 1][0]

    while qj >= 0 and tasks[qj][1] > sj:
        qj -= 1

    return qj + 1

opt_cnt = 0
def opt(n):
    global opt_cnt
    opt_cnt += 1

    if n == 0:
        return 0

    qj = q(n)
    opt_prev = opt(n - 1)
    opt_sum = tasks[n - 1][2] + opt(qj)

    if opt_prev >= opt_sum:
        opt_curr = opt_prev
    else:
        opt_curr = opt_sum

    return opt_curr

opts = [0] + [-1] * n
opt_memo_cnt = 0
def opt_memo(i):
    global opt_memo_cnt
    opt_memo_cnt += 1

    if opts[i] != -1:
        return opts[i]

    qj = q(i)
    opt_prev = opt_memo(i - 1)
    opt_sum = tasks[i - 1][2] + opt_memo(qj)

    if opt_prev >= opt_sum:
        opt_curr = opt_prev
    else:
        opt_curr = opt_sum

    opts[i] = opt_curr
    return opt_curr

print('opt:', opt(n))
print('calls:', opt_cnt)
print('opt:', opt_memo(n))
print('calls:', opt_memo_cnt)