#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):

    # sln i found online:
    # an array of 6 zeros - numbers can only be 1,2,3,4 or 5
    # create 6 slots, first slot is allocated for 0
    count = [0] * 6
    
    for bird in arr:
        count[bird] += 1
    # obtain an array filled with the frequencies of different numbers

    print(count)

    # max gets you the first value 
    return count.index(max(count))

    # my sln - passed 5/6 test cases:
    # print(count)
    # freq = []
    # arr.sort()
    # # [1, 1, 2, 2,]
    # count = 1
    # for i in range(len(arr) - 1):
    #     if (arr[i] == arr[i+1]):
    #         count += 1
    #     elif (arr[i] != arr[i+1]):
    #         freq.append(count)
    #         count = 1
    # if (arr[len(arr) - 2] != arr[len(arr) - 1]):
    #     freq.append(1)

    # # print(arr)
    # # print(freq)
    # arr2 = list(set(arr))
    # # print(arr2)
    # # print(max(freq))
    # for i in range(len(freq)):
    #     if (freq[i] == max(freq)):
    #         return (arr2[i])


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# arr = [1,1,2,2,3]
result = migratoryBirds(arr)
print(result)