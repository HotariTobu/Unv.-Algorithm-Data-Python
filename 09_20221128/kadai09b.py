from typing import Tuple

def findat(l: list, k: int) -> Tuple[list, int]:
    l.sort()
    return l, l[k - 1]

a = [int(token) for token in input().split()]
k = int(input())

sorted_a, min_k = findat(a, k)
print(sorted_a)
print(min_k)