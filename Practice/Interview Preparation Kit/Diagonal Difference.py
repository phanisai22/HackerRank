#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    a = 0
    b = 0
    for i in range(len(arr)):
        a += arr[i][i]
    
    for i in range(len(arr)):
        b += arr[len(arr) - i - 1][i]
    
    s = b - a
        
    return abs(s)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

