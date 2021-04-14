n, m = tuple(map(int, input().split()))
s = 0
p = list(map(int, input().split()))
p = sorted(p)
for item in p:
    if item < m:
        m = 2*(m - item)
        s += 1

print(s)