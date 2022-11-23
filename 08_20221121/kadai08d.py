from typing import Tuple

a = [int(token) for token in input().split()]

# 2つのソート済みの姓数列を併合させる関数
def inversion_with_merge(a1: list, a2: list) -> Tuple[int, list]:
    k3 = 0
    a = []

    while (a1 and a2):
        if (a1[0] > a2[0]):
            k3 += len(a1)
            a.append(a2.pop(0))
        else:
            a.append(a1.pop(0))
    
    return k3, a + a1 + a2

# 再帰呼び出しに用いる関数
def inversion_with_merge_sort(a: list) -> Tuple[int, list]:
    n = len(a)
    if n < 2:
        return 0, a
    else:
        m = n // 2

        k1, a1 = inversion_with_merge_sort(a[:m])
        k2, a2 = inversion_with_merge_sort(a[m:])

        k3, result = inversion_with_merge(a1, a2)

        return k1 + k2 + k3, result

inversion, _ = inversion_with_merge_sort(a)
print(inversion)