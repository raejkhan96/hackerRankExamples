#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    arr = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i in abc:
            x = abc.index(i) 
            arr.append(h[x])
            # print(x)
    # print(arr)
    # print(max(arr))
    # print(len(word))
    return (max(arr) * len(word))


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = "torn"
result = designerPdfViewer(h, word)
print(result)