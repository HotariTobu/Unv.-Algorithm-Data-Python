# 再起呼び出しに用いる関数
def findat(l: list, k: int) -> int:
    print('input:', l, 'k =', k)

    n = len(l)
    if n < 5:
        l.sort()
        min_k = l[k - 1]
    else:
        pivot = l[0]

        L = []
        R = []
        for i in range(1, n):
            e = l[i]
            if e < pivot:
                L.append(e)
            else:
                R.append(e)

        len_L = len(L)

        if len_L >= k:
            min_k = findat(L, k)
        elif len_L == k - 1:
            min_k = pivot
        else:
            min_k = findat(R, k - len_L - 1)

    print('return:', min_k)
    return min_k

a = [int(token) for token in input().split()]
k = int(input())

print('answer:', findat(a, k))