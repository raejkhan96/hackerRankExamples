#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):

    # actual solution 
    keyboards.sort()
    drives.sort()
    # print(keyboards)
    # print(drives)
    res = -1
    for k in keyboards:
        x = -1
        for d in drives:
            if k + d <= b:
                x = k + d
        if x == -1:
            break
        else:
            res = max(res, x)
    return res

    # My solution - didnt pass all tests
    # arr = []
    # sorted_keyboards = sorted(keyboards, reverse=True)
    # for i in range(len(sorted_keyboards)):
    #     if (sorted_keyboards[i] < b):
    #         start = i
    #         break;

    # for j in range(start, len(sorted_keyboards)):
    #     for k in range(len(drives)):
    #         if ((sorted_keyboards[j] + drives[k]) < b):
    #             arr.append(sorted_keyboards[j] + drives[k])

    # if not arr:
    #     return('-1')
    # else:
    #     return(max(arr))

b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)