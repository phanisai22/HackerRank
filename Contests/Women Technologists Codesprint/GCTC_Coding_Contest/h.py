def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):

            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False

def findLong(a, n):

    ans = []
    m = 0
    t = 0
    for i in range(n):
        
        if i != n - 1 and a[i] < a[i + 1]:
            t += 1
        else:
            if m < t:
                m = t
                t = 0
                ans = a[i - m:i + 1]

    ans = [str(i) for i in ans]
    ans = ' '.join(ans)
    return ans



t = int(input())
l = list(map(int, input().split()))
p = []

for item in l:
    if isPrime(item):
        p.append(item)

print(findLong(p, len(p)))
