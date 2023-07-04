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
    total = n
    num_s = total - 1
    num_h = 1
    # Write your code here
    for col in range(total):
        for space in range(num_s):
            print(" ", end = "")
        for hash in range(num_h):    
            print("#", end = "")
        print("")
        num_s -= 1
        num_h += 1


n = 10
staircase(n)