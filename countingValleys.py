import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# need to figure out what to print on each layer and then concatenate them 

# Misunderstood this problem, thought i had to draw valleys
# Found solution online 

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    num_valley = 0

    for i in s:
        if i == "U":
            level = level+1
        if i == "D":
            level = level -1
        if(level == 0 and i == "U"):
            num_valley += 1
    return num_valley


steps = 8
path = 'UDDDUDUU'
result = countingValleys(steps, path)
print(result)


# print('_/\\' + "\n" + 3*" " + "\\")