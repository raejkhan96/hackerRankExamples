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

def countingValleys(steps, path):
    # Write your code here
    ans = '_'
    for letter in path:
        if(letter == 'U'):
            ans += '/'
        else:
            ans += '\\'
    ans += '_'
    return ans



steps = 8
path = 'UDDDUDUU'
result = countingValleys(steps, path)
print(result)