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
    # Write your code here
    num_ans = x1 - x2
    rate = v2 - v1
    x = num_ans/rate
    if (x > 0):
        return 'YES'
    else:
        return 'NO'

x1 = 0
v1 = 2
x2 = 5
v2 = 3
result = kangaroo(x1, v1, x2, v2)
print(result)