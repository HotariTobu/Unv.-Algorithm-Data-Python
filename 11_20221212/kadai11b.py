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

opts = [0]
def opt(j):
    opts_len = len(opts)
    if opts_len > j:
        return opts[j]

    for i in range(opts_len, j):
        opt(i)

    qj = q(j)
    opt_prev = opt(j - 1)
    opt_sum = tasks[j - 1][2] + opt(qj)

    if opt_prev >= opt_sum:
        opt_curr = opt_prev
    else:
        opt_curr = opt_sum

    opts.append(opt_curr)
    return opt_curr

for j in range(1, n + 1):
    print('opt', j, '=', opt(j))