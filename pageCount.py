#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    # SLN from online, much simpler than mine:
    # complete floor division, truncates to lowest integer
    page_in_book = p//2
    total_pages = n//2
    print(page_in_book)
    print(total_pages)
    from_front = page_in_book # in order to get the amount of pages from front, you just need p//2
    from_back = total_pages - page_in_book #the back is just the total - front
    return(min(from_front,from_back))

    # MY SOLUTION:
    # arr1, arr2 = [], []
    # count1, count2 = 0, 0
    # arr1.append([1])
    # # forwards
    # for i in range(2, n, 2):
    #     arr1.append([i, i+1])
    # # print(arr1)
    # for i in range(len(arr1)):
    #     if p in arr1[i]:
    #         break
    #     else:
    #         count1 += 1
    # # backwards 
    # arr2 = arr1[::-1]
    # # print(arr2)
    # for j in range(0, len(arr2)):
    #     print(arr2[j])
    #     if p in arr2[j]:
    #         break
    #     else:
    #         count2 += 1
    # # print("COUNT1 ", count1)
    # # print("COUNT2 ", count2)
    # return min(count1, count2)

n = 5
p = 4
result = pageCount(n, p)
print(result)