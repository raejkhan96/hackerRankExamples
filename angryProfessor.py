#!/bin/python3

import math 
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    # need to count the amount of values are before and at  0
    # if it matches k, return NO, else YES
    count = 0
    for x in a:
        if (x <= 0):
            count +=1 
    if (count >= k):
        return 'NO'
    return 'YES'

k = 3
a = [-2, -1, 0, 1, 2]
result = angryProfessor(k, a)
print(result)