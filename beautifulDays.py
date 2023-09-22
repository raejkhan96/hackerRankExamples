#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

# Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

def beautifulDays(i, j, k):
    # Write your code here

    # count for beautiful days
    count = 0 

    # Step 0 - go through the array 
    for num in range(i, j+1):

    # Step 1 - reverse the number
    # num = 120
        reversed_num = 0
        value = num
        while num != 0:
            #  modulo 10 gets the last digit of the number. eg: 1234 % 10 = 4. We divide the number by 10 to get the remainder
            digit = num % 10 
            # the reversed number is itself x 10 - to move it to the left, then the next digit in line
            # eg: first iteration digit is 4, reversed number is 4
            # second iteration digit is 3, reversed number is 43
            # and so on...
            reversed_num = reversed_num * 10 + digit
            # then we divide the number by 10 to keep going
            # 1234 becomes 123 for the next loop
            num //= 10

        # step 2, determine if it is a whole number
        x = (abs(value - reversed_num))/k
        # print(value)
        # print(reversed_num)
        # print(x)

        # step 3, if it is a whole number, up the count 
        if (x.is_integer() == True):
            count += 1

    return count

ans = beautifulDays(20, 23, 6)
print(ans)