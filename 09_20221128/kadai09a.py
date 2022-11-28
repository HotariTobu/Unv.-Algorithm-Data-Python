def quicksort(l: list) -> list:
    print('input:', l)

    if len(l) <= 1:
        result = l
    else:
        pivot = l[0]
        L = [e for e in l if e < pivot]
        R = [e for e in l if e > pivot]

        L = quicksort(L)
        R = quicksort(R)

        result = L + [pivot] + R

    print('return:', result)
    return result

a = [int(token) for token in input().split()]
print('answer:', quicksort(a))