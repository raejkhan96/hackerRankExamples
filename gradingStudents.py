#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        # j = 0
        for j in range(grades[i]+1, 101):
            # print(grades[i])
            # print(j)
            if ((j % 5 == 0) and ((j - grades[i]) < 3) and (grades[i] >= 38)):
                grades[i] = j
                break

    return grades

grades = [73, 67, 38, 33]
result = gradingStudents(grades)
print(result)