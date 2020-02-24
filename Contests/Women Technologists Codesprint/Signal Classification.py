#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'classifySignals' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY freq_standard
#  2. INTEGER_ARRAY freq_signals
#

def classify_signals(freq_standard, freq_signals):
    res = []


    return res


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    f = list(map(int, input().rstrip().split()))

    F = list(map(int, input().rstrip().split()))

    ans = classify_signals(f, F)

    for item in ans:
        print(ans)
