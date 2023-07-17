#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    ar.sort()
    # print(ar)
    for i in range(n - 1):
        for j  in range(i + 1, n):
            if ((ar[i] +  ar[j]) % k == 0):
                count += 1

    return count

n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
result = divisibleSumPairs(n, k, ar)
print(result)