#!/bin/python3

import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        if not word in d:
            d[word] = 1
        else:
            d[word] += 1

    for word in note:
        if word in d:
            if d[word] > 0:
                d[word] -= 1


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
