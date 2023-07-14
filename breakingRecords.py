#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min, max = scores[0], scores[0]
    min_count, max_count = 0, 0
    arr = []
    for i in range(1, len(scores)):
        if scores[i] > max:
            # print("new max", scores[i])
            max_count += 1
            max = scores[i]
        elif scores[i] < min:
            # print("new min", scores[i])
            min_count +=1
            min = scores[i]
    arr.append(max_count)
    arr.append(min_count)
    return arr

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
ans = breakingRecords(scores)
print(ans)