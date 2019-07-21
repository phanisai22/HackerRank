#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    sea_level = 0  # Assuming a graph and sea level at x axis intially as 0.
    no_of_valleys = 0
    for i in range(len(s)):
        if s[i] == "U":
            sea_level += 1
        elif s[i] == "D":
            sea_level -= 1

        if sea_level == 0 and s[i] == "U":
            no_of_valleys += 1

    return no_of_valleys


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
