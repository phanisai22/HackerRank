#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = 0
    for item in arr:
        s += item
    
    mi = arr[0]
    for item in arr[1:]:
        if mi > item:
            mi = item

    ma = arr[0]
    for item in arr[1:]:
        if ma < item:
            ma = item
    
    mis = s - ma
    mas = s - mi

    print(mis, end= " ")
    print(mas)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
