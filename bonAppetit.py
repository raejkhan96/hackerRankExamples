#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    b_charged = b
    sum = 0
    for i in range(len(bill)):
        if (i == k):
            next
        else:
            sum += bill[i]
    b_actual = (sum/2)
    # print(sum)
    # print(b_actual)
    if (b_charged == b_actual):
        print("Bon Appetit")
    else: 
        print(int(b_charged - b_actual))
    


        


bill = [3, 10, 2, 9]
k = 1
b = 12
bonAppetit(bill, k, b)