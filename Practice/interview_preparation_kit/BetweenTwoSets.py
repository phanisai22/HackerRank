import math
import os
import random
import re
import sys


def gcda(x, y):
    while(y):
        x, y = y, x % y

    return x


def gcd(x):
    r = x[0]
    for i in range(1, len(x)):
        r = gcda(r, x[i])

    return r


def lcma(x, y):
    return (x*y)//gcda(x, y)


def lcm(x):
    r = x[0]
    for i in range(1, len(x)):
        r = lcma(r, x[i])

    return r

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    k = lcm(a)
    l = gcd(b)
    c = 0
    i = k
    j = 2
    while i <= l:
        if l % i == 0:
            c += 1

        i = k * j
        j += 1
    
    return c


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
