#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    height = 1
    for num in range(0, n):
        print("PERIOD ", num)
        if num % 2 == 0:
            height = height * 2
            print("HEIGHT: ", height)
        elif (num != 0):
            height = height + 1
            print("HEIGHT: ", height)
n = 5
result = utopianTree(n)
print(result)