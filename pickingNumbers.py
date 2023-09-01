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
   
    big_arr = []
    new_arr = []

    # print(a)
    for i in range(len(a) - 1):
        
        current = i
        next = i+1
        # print("ROUND ", i)
        # print(a[current])
        # print(a[next])
    
        if (abs(a[next] - a[current]) > 1):
            # print("BREAK")
            new_arr.append(a[current])
            big_arr.append(new_arr)
            new_arr = []
            # print(new_arr)
            # print(a[next], a[current])
        else:
            new_arr.append(a[current])
            
    new_arr.append(a[current])    
    big_arr.append(new_arr)        
    # print(big_arr)

    # this gets you the largest sub array
    largest_array = max(big_arr, key=len)
    # print(largest_array)
    # this gets you the largest array length
    largest_array_len = len(largest_array)
    # print(largest_array_len)
    return largest_array_len

a = [4, 6, 5, 3, 3, 1]
# a = [1,1,2,2,4,4,5,5,5]
result = pickingNumbers(a)
print(result)