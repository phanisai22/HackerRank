import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    
    r = []
    j = (len(s) - m) + 1

    c = 0
    for i in range(j):
        if sum(s[i:i+m]) == d:
            c += 1
    
    return c

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
