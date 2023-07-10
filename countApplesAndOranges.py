#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_landing, oranges_landing = [], []
    count_apples, count_oranges = 0, 0
    for i in range(len(apples)):
        apples_landing.append(apples[i] + a)
    for i in range(len(oranges)):
        oranges_landing.append(oranges[i] + b)

    for i in range(len(apples_landing)):
        if (s <=  apples_landing[i] <= t):
            count_apples += 1
    for i in range(len(oranges_landing)):
        if (s <=  oranges_landing[i] <= t):
            count_oranges += 1

    # print(apples_landing)
    # print(oranges_landing)
    print(count_apples)
    print(count_oranges)


s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)