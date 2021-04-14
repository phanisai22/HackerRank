k = int(input())
s = 0
n = list(map(int, input().split()))
n = sorted(n, reverse=True)

for i in range(k):
    s += n[0]
    n = n[1:]

    for j in range(k - (i + 1)):
        if n[j] == 0:
            continue
        n[j] -= 1

print(s)
