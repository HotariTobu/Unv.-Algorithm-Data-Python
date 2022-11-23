H, W = [int(token) for token in input().split()]
a = [int(token) for token in input().split()]

count = 0

h = H
w = W

for l in a[::-1]:
    h_count = (h // l)
    w_count = (w // l)

    count += h_count * (W // l)
    count += w_count * (H // l)
    count -= h_count * w_count
    
    h %= l
    w %= l

print(count)