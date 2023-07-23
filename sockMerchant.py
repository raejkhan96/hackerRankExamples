import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar2 = set(ar)
    even = []
    print(ar2) 
    
    for num in ar2:
        # print(num)
        count = 0
        for i in range(0, len(ar)): 
            if (ar[i] == num):
                count += 1
        print(num, count)
        if count % 2 == 0:
            even.append((count/2))
        else:
            even.append((count-1)/2)
    
    # print(even)
    count = 0
    for i in range(len(even)):
        count += even[i]
    return(int(count))


n = 7
ar = [1, 2, 1, 2, 1, 2, 3]
result = sockMerchant(n, ar)
print(result)
