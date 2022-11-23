from operator import itemgetter

n = int(input())
lines = [input().split() for _ in range(n)]
tasks = [(int(tokens[0]), int(tokens[1])) for tokens in lines]

s = []

tasks.sort(key=itemgetter(1))

t = 0

for task in tasks:
    s.append(t)
    t = t + task[0]

hot_task = max(zip(tasks, s), key=lambda task: max(0, task[0][0] + task[1] - task[0][1]))

print(hot_task[0][0] + hot_task[1] - hot_task[0][1])