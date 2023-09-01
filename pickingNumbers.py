#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    # go through array
    # do a for loop within a for loop
    # outer for loop should should be previous number
    # inner for loop current number
    # compare previous number with current number
    # if difference is less than one, add to subarray
    # if not, move on and start again
    # then find max length

    big_arr = []
    new_arr = []
    for i in range(len(a) - 1):
        
        current = i
        next = i+1
        print(a[current])
        print(a[next])
        if (abs(a[next] - a[current]) > 1):
           new_arr.append(a[current])
           big_arr.append(new_arr)
           new_arr = []
           print(new_arr)
           print(a[next], a[current])
        else:
            new_arr.append(a[current])
    return big_arr 


a = [1,1,2,2,4,4,5,5,5]
result = pickingNumbers(a)
print(result)