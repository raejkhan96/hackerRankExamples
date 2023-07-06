import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def birthdayCakeCandles(ar):
    # Write your code here
    c = 0
    large = max(ar)
    for i in range(0,len(ar)):
        if ar[i] == large:
            c = c + 1
    return c


candles = [4, 4, 1, 2, 4, 4, 4]
result = birthdayCakeCandles(candles)
print(result)