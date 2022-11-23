from unittest import result


n = int(input())

def f(n: int) -> int:
    def dump(re: int):
        print('f(', n, ') = ', re, sep='')
        
    if n < 2:
        dump(n)
        return n
    else:
        result = f(n - 1) + f(n - 2)
        dump(result)
        return result

print('answer:', f(n))