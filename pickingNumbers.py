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
# https://shounaklohokare.medium.com/picking-numbers-hackerrank-solution-in-python-bf64005c2e98

from collections import Counter
def pickingNumbers(a):
    countNums = Counter(a)
    maxnum=0        
    print(countNums)
    print(countNums[0])
    print(countNums[1])
    print(countNums[2])
    print(countNums[3])
    for i in range(1, 100):
        maxnum = max(maxnum, countNums[i]+countNums[i+1])                      
        
    return maxnum

    #     current = i
    #     next = i+1
    #     # print("ROUND ", i)
    #     # print(a[current])
    #     # print(a[next])
    
    #     if (abs(a[next] - a[current]) > 1):
    #         # print("BREAK")
    #         new_arr.append(a[current])
    #         big_arr.append(new_arr)
    #         new_arr = []
    #         # print(new_arr)
    #         # print(a[next], a[current])
    #     else:
    #         new_arr.append(a[current])
            
    # new_arr.append(a[current])    
    # big_arr.append(new_arr)        
    # # print(big_arr)

    # # this gets you the largest sub array
    # largest_array = max(big_arr, key=len)
    # # print(largest_array)
    # # this gets you the largest array length
    # largest_array_len = len(largest_array)
    # # print(largest_array_len)
    # return largest_array_len

a = [4, 6, 5, 3, 3, 1]
# a = [1,1,2,2,4,4,5,5,5]
result = pickingNumbers(a)
print(result)