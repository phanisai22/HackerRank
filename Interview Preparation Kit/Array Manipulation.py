#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


# def arrayManipulation(n, queries):
#     arr = [0]*n
#     for i in queries:
#         for j in range(i[0]-1, i[1]):
#             arr[j] += i[2]

#     return max(arr)

n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y) <= len(list)):
        list[y] -= incr
max = x = 0
for i in list:
   x = x+i
   if(max < x):
       max = x
print(max)

# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])

#     queries = []

#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = arrayManipulation(n, queries)
#     print(result)
