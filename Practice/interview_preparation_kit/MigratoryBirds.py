import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d = {}
    for t in arr:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    m = max(d.values())
    l = []
    for key, value in d.items():
        if value == m:
            l.append(key)
        
    return min(l)

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)