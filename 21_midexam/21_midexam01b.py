n = int(input())
students = [input().split() for _ in range(n)]
# scores = [(int(id), int(score)) for (id, firstname, lastname, score) in students]

# print(scores)

# scores.sort(key=lambda score: score[1])

students.sort(key=lambda student: int(student[0]))
students.sort(key=lambda student: int(student[3]), reverse=True)

for student in students:
    print(*student)