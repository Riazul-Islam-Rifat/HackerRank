#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    space=' '
    symbol='#'
    for item in range(n-1):
        print(space*(n-(item+2)),symbol*(item+1))
    print(symbol*n)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
