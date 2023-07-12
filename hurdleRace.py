#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    big = max(height)
    ans = 0
    if (big > k):
        ans = big - k
    return ans

height = [1, 6, 3, 5, 2]
k = 4
ans = hurdleRace(k, height)
print(ans)