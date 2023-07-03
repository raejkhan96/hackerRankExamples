#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    den = len(arr)
    pos, neg, zeroes = 0, 0, 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zeroes += 1

    pos_ratio = pos/den
    neg_ratio = neg/den
    zero_ratio = zeroes/den

    formatted_pos = "{:.6f}".format(pos_ratio)
    formatted_neg = "{:.6f}".format(neg_ratio)
    formatted_zero = "{:.6f}".format(zero_ratio)

    print(formatted_pos)
    print(formatted_neg)
    print(formatted_zero)

arr = [1, 1, 0, -1, -1]
plusMinus(arr)