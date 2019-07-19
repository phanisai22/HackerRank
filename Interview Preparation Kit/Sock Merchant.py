#!/bin/python3

import math
import random
import re
import sys
from collections import Counter


def sockMerchant(n, ar):
    if 1 <= n <= 100:
        counter_set = Counter(ar)
        unique_set = list(set(ar))
        pair_of_socks = 0

        for i in range(len(unique_set)):
            count = int(counter_set[unique_set[i]])
            pair_of_socks += int(count / 2)

        print(pair_of_socks)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    sockMerchant(n, ar)
