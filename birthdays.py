#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

# couldnt get this one, needed help
def birthday(s, d, m):

    count = 0
    # Write your code here
    for i in range((len(s) - m) + 1):
         # create an array from the first point plus the month
         # Get the segment (window) of size m starting from index i
        # print(i+m)
        segment = s[i:i + m]
        # print(segment)
        # Check if the sum of the segment is equal to Ron's birth day
        if sum(segment) == d:
            count += 1
    
    return count

s = [2, 2, 1, 3, 2]
d = 4
m = 2
ans = birthday(s, d, m)
print(ans)