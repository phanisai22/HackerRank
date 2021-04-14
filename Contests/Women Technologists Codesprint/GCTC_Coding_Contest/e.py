import math
t, m = tuple(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
g = sorted(g)
b = sorted(b)

if b[0] < g[0]:
    print(-1)
else:
    if t%m == 0:
        s = t//m
    else:
        s = t//m
        s += 1

print(s)