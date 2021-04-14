nl, l = list(map(int, input().split()))
nm , m = list(map(int, input().split()))

l = [str(i) for i in range(l, m + 1)]
l = ''.join(l)
l = sorted(l)
temp = 0
for item in l:
    if item == 0:
        temp += 1
    else :
        break
    
l = l[temp:]
l = ''.join(l)
print(l)

