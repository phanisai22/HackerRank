#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     swaps = 0
#     for i in range(len(arr)):
#         if arr[i] != i+1:
#             swaps += 1
#             arr[arr.index(i+1)], arr[i] = arr[i], arr[arr.index(i+1)]

#     return swaps


def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)
