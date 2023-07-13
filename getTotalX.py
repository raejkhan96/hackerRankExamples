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

    # OBTAINED SOLUTION:
    # maximum of a is required because if you check the max - you dont need the rest
    max_a = max(a)
    # minium of b is required because we need all the values/factors to be in common - so we take the lowest value
    min_b = min(b)
    count = 0

    # min_b +1 because we are up to and not including
    for num in range(max_a, min_b + 1):
        if all(num % factor == 0 for factor in a) and all(factor % num == 0 for factor in b):
            count += 1

    return count

    # MY SOLUTION - DOES NOT WORK:
    # # Write your code here
    # factors, factors2 = [], []
    # # Go through the entire array b
    # for i in range(len(b)):
    #     # for each number in array b
    #     for j in range(2, b[i]):
    #         # find the factors of each number
    #         if ((b[i] % j) == 0):
    #             factors.append(j)

    # #  first part needs to be reworked. as opposed to adding everything find the factors in common 
    
    # print(factors)
    # factors_no_duplicates = set(factors)
    # print(factors_no_duplicates)
    # factors_no_duplicates = list(factors_no_duplicates)
    # print(factors_no_duplicates)

    # # i, j = 0, 0
    # for i in range(len(b)):
    #     for j in range(len(factors_no_duplicates) - 1):
    #         print(j)
    #         print(factors_no_duplicates[j])
    #         if (b[i] % factors_no_duplicates[j] != 0):
    #             factors_no_duplicates.remove(factors_no_duplicates[j])

    # # print(factors_no_duplicates)
    # # for c in range(len(a)):
    # #     print(a[c])

    # for k in range(len(factors_no_duplicates)):
    #     count = 0
    #     for c in range(len(a)):
    #         if ((factors_no_duplicates[k] % a[c]) == 0):
    #             count += 1
    #     if (count == len(a)):
    #         factors2.append(factors_no_duplicates[k])

    # print(factors2)

    # return len(factors2)


       
    
    # # factors3 = set(factors2)
    # # print(factors3)
    # # return len(factors3)

                       



a = [2, 6]
b = [24, 36]
ans = getTotalX(a, b)
print(ans)
