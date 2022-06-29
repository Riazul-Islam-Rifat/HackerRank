#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    c1 = 0
    c2 = 0
    c3 = 0
    for item in arr:
        if item == 0:
            c1 = c1 + 1
        elif item > 0:
            c2 = c2 + 1
        else:
            c3 = c3 + 1
    print(format(c2 / n, '.6f'))
    print(format(c3 / n, '.6f'))
    print(format(c1 / n, '.6f'))


if __name__ == '__main__':
    n = input()

    arr = list(map(int, n.split(" ")))

    plusMinus(arr)
