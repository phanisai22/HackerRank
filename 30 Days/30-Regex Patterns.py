#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        pattern_name = '[a-z]'
        if re.match(pattern_name, firstName):
            print(firstName[N])

# Incomplete
