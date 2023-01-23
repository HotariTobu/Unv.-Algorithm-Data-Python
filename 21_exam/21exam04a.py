n = int(input())

cache = [0, 0, 1]
def a(i):
    cache_size = len(cache)
    if cache_size < i:
        for j in range(cache_size, i):
            cache.append(a(j))
            
    return sum(cache[i - 3:i])

print(a(n))