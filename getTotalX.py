#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    factors, factors2 = [], []
    # Go through the entire array b
    for i in range(len(b)):
        # for each number in array b
        for j in range(2, b[i]):
            # find the factors of each number
            if ((b[i] % j) == 0):
                factors.append(j)

    #  first part needs to be reworked. as opposed to adding everything find the factors in common 
    
    print(factors)
    factors_no_duplicates = set(factors)
    print(factors_no_duplicates)
    factors_no_duplicates = list(factors_no_duplicates)
    print(factors_no_duplicates)

    for c in range(len(a)):
        print(a[c])

    for k in range(len(factors_no_duplicates)):
        count = 0
        for c in range(len(a)):
            if ((factors_no_duplicates[k] % a[c]) == 0):
                count += 1
        if (count == len(a)):
            factors2.append(factors_no_duplicates[k])

    print(factors2)

    return 5


       
    
    # factors3 = set(factors2)
    # print(factors3)
    # return len(factors3)

                       



a = [2, 6]
b = [24, 36]
ans = getTotalX(a, b)
print(ans)
