#!/bin/python3

import math
import os
import random
import re
import sys
import string

def solve(s):
    return s.capwords(s, " ") 


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "1 2 2 3 4 5 6 7 8  9" 

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
