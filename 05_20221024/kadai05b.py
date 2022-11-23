from operator import itemgetter

n = int(input())
lines = [input().split() for _ in range(n)]
tasks = [(int(tokens[0]), int(tokens[1])) for tokens in lines]

J = []

tasks.sort(key=itemgetter(1))

t = min(tasks, key=itemgetter(0))[0]

for task in tasks:
    if t <= task[0]:
        J.append(task)
        t = task[1]

print(len(J))