#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    arr1, arr2 = [], []
    count1, count2 = 0, 0
    # forwards
    for i in range(2, n, 2):
        arr1.append([i, i+1])
    # print(arr1)
    for i in range(len(arr1)):
        count1 += 1
        if p in arr1[i]:
            break
    # backwards 
    for j in range(n-1, 0, -2):
        arr2.append([j, j-1])
    # print(arr2)
    for j in range(len(arr2)):
        count2 += 1
        if p in arr2[j]:
            break

    return min(count1, count2)

n = 6
p = 2
result = pageCount(n, p)
print(result)