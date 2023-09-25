#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

# https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

def viralAdvertising(n):
    a = 5
    cumulative = 0 
    # Write your code here
    for day in range(1, n+1):
        # print("DAY ", day)
        like = (a // 2) 
        # print(" LIKED ", like)
        shared = like * 3
        cumulative = cumulative + like
        # print("CUMULATIVE ", cumulative)
        a = shared

    return cumulative

n = 3
ans = viralAdvertising(n)
print(ans)