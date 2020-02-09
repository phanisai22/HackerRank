#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input())
    c = list(map(int, input().rstrip().split()))

    if c[0] == c[n-1] == 0 and 2 <= n <= 100:
        
        jumps = 0
        i = 0

        while i < n -1:
            if i + 2 >= n or c[i + 2] == 1:
                i += 1
                jumps += 1
            else:
                i += 2
                jumps += 1
        
        print(jumps)
