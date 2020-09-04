#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    p = 0
    o = 0

    for i in range(len(apples)):
        if s <= apples[i] + a <= t:
            p += 1

    for i in range(len(oranges)):
        if s <= oranges[i] + b <= t:
            o += 1

    print(p)
    print(o)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
