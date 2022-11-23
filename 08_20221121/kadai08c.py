a = [int(token) for token in input().split()]

# 2つのソート済みの姓数列を併合させる関数
def merge(a1: list, a2: list) -> list:
    a = []

    while (a1 and a2):
        if (a1[0] > a2[0]):
            a.append(a2.pop(0))
        else:
            a.append(a1.pop(0))
    
    return a + a1 + a2

# 再帰呼び出しに用いる関数
def merge_sort(a: list) -> list:
    print('input:', a)

    n = len(a)
    if n < 2:
        result = a
    else:
        m = n // 2

        a1 = merge_sort(a[:m])
        a2 = merge_sort(a[m:])

        result = merge(a1, a2)

    print('return:', result)
    return result


print('answer:', merge_sort(a))