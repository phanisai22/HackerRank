#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):

    count = s.count("a")
    divisor = int(n/len(s))
    no_of_a_s = count * divisor

    remaining_digits = n % len(s)
    remaining_str = s[:remaining_digits]
    no_of_a_s += remaining_str.count("a")

    return no_of_a_s


if __name__ == '__main__':
    s = input()
    n = int(input())
    print(repeatedString(s, n))
