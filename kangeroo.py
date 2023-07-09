#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Actual sln - not sure of difference between my sln and given sln
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

    # MY SLN - DOES NOT PASS ALL TEST CASES:
    # num_ans = x1 - x2
    # rate = v2 - v1
    # x = num_ans/rate
    # if ((x > 0) and (type(x) is int)):
    #     return 'YES'
    # else:
    #     return 'NO'

x1 = 21
v1 = 6
x2 = 47
v2 = 3
result = kangaroo(x1, v1, x2, v2)
print(result)