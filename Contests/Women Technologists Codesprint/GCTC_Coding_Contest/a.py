k = int(input())
s = 0
n = input().split()

for item in n:
    item = item[0]

    s += int(item)

s = str(s)
print(s[0])