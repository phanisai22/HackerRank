# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:26:53 2019

@author: uppup
"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(0, n):
        print(arr.pop(), end=' ')