a1 = [int(token) for token in input().split()]
a2 = [int(token) for token in input().split()]

# 2つのソート済みの姓数列を併合させる関数
def merge(a1: list, a2: list) -> list:
    a = []

    while (a1 and a2):
        if (a1[0] > a2[0]):
            a.append(a2.pop(0))
        else:
            a.append(a1.pop(0))
    
    return a + a1 + a2

print(merge(a1, a2))