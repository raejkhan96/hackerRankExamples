#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum, max_sum = 0, 0
    for i in range(4):
        min_sum += arr[i]

    for j in range(1, 5):
        max_sum += arr[j]

    print(min_sum, max_sum)



arr = [9,7,3,5,1]
miniMaxSum(arr)
