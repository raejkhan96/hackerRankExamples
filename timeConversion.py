#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ans = s
    if ((s[:2] == '12') and (s[8] == 'A')):
        ans = s.replace('12', '00')
       
    if (s[8] == 'P'): 
        if (int(s[:2]) < 12):
            old_time = int(s[:2])
            if old_time < 10:
                old_time_string = '0' + str(old_time)
            else:
                old_time_string = str(old_time)
            new_time = old_time + 12
            new_time_string = str(new_time)
            ans = s.replace(old_time_string, new_time_string)
            
    ans = ans.replace('AM', '')  
    ans = ans.replace('PM', '')
    return ans


s = '12:45:54PM'
ans = timeConversion(s)
print(ans)