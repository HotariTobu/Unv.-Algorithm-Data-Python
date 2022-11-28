import math

# リストをチャンク分けする関数
def div(l: list, n: int) -> list:
    for i in range(0, len(l), n):
        yield l[i:i + n]

# 再起呼び出しに用いる関数
def findat(l: list, k: int) -> int:
    print('input:', l, 'k =', k)

    n = len(l)
    if n < 5:
        l.sort()
        min_k = l[k - 1]
    else:
        chunks = list(div(l, 5))

        last_chunk = chunks.pop()
        if len(last_chunk) == 5:
            chunks.append(last_chunk)

        medians = [sorted(chunk)[2] for chunk in chunks]

        pivot = findat(medians, math.ceil(len(medians) / 2))

        L = [e for e in l if e < pivot]

        len_L = len(L)

        if len_L >= k:
            min_k = findat(L, k)
        elif len_L == k - 1:
            min_k = pivot
        else:
            R = [e for e in l if e > pivot]
            min_k = findat(R, k - len_L - 1)

    print('return:', min_k)
    return min_k

a = [int(token) for token in input().split()]
k = int(input())

print('answer:', findat(a, k))