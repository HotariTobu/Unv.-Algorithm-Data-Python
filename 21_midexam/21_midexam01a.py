n = int(input())
bits_list = [input() for _ in range(n)]

def is_suf(bits_list: list):
    bits_list.sort(key=len)
    n = len(bits_list)

    for i, bits in enumerate(bits_list):
        for j in range(i + 1, n):
            if bits_list[j].startswith(bits):
                return False
    
    return True

print('yes' if is_suf(bits_list) else 'no')