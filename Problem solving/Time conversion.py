#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = list(map(str, s.split(":")))
    pm_convert = ""
    am_convert = '00:'
    if "P" in s:
        if int(time[0])<12:
            time[0] = str(int(time[0]) + 12)
            for item in range(len(time)):
                if item == len(time) - 1:
                    pm_convert += time[item][0] + time[item][1]
                else:
                    pm_convert += time[item] + ":"
        else:
            for item in range(0, len(time)):
                if item == len(time) - 1:
                    pm_convert += time[item][0] + time[item][1]
                else:
                    pm_convert += time[item] + ":"
        return pm_convert
    else:
        if int(time[0]) == 12:
            for item in range(1, len(time)):
                if item == len(time) - 1:
                    am_convert += time[item][0] + time[item][1]
                else:
                    am_convert += time[item] + ":"
            return am_convert
        else:
            time_am=''
            for item in range(0, len(time)):
                if item == len(time) - 1:
                    time_am += time[item][0] + time[item][1]
                else:
                    time_am += time[item] + ":"
            return time_am
s = input()

result = timeConversion(s)
print(result)