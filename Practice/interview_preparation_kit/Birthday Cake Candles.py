#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    d = {}
    for item in ar:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    
    ma = d[ar[0]]
    for item in d:
        if ma < d[item]:
            ma = d[item]
    
    return ma

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)

