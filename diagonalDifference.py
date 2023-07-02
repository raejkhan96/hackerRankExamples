
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diag = 0
    right_diag = 0
    print("LENGTH OF THE ARR: ", len(arr))
    for i in range(0,len(arr)):
        # left diag - 0,0 - 1,1 - 2,2
        # print("LEFT NUMBERS ", arr[i][i])
        left_diag = left_diag + arr[i][i]
    
    for j in range(0,len(arr)):
        # right diag - 0,2 - 1,1  - 2,0
        right_diag = right_diag + arr[j][len(arr)-1-j]
    
    diff = abs(left_diag - right_diag)
    return diff
        

arr = [[11,2,4], [4,5,6], [10,8,-12]]
result = diagonalDifference(arr)
print("ABSOLUTE DIFFERENCE OF DIAGONAL", result)