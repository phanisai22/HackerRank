#!/bin/python3

import math
import os
import random
import re
import sys

def rotLeft(a, d):
    return a[d : ] + a[ : d] 


if __name__ == '__main__':

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    for ele in result:
        print(ele, end=" ")