#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    m = 0
    z = 0
    p = 0
    for item in arr:
        if item < 0:
            m += 1
        elif item == 0:
            z += 1
        else:
            p += 1
    l = len(arr)
    print("{0:.6f}".format(p/l))
    print("{0:.6f}".format(m/l))
    print("{0:.6f}".format(z/l))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
