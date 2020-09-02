#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = s.strip()
    h, m, s = map(int, t[:-2].split(':'))
    f = t[-2:]
    h = h % 12 + (f.upper() == "PM") *12
    return (('%02d:%02d:%02d') % (h, m, s))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
