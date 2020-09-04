import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = 0
    worst = 0
    mi = scores[0]
    ma = scores[0]

    for i in range(1, len(scores)):
        if scores[i] > ma:
            ma = scores[i]
            best+= 1
        elif scores[i] < mi:
            mi = scores[i]
            worst+= 1

    return [best, worst]

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)