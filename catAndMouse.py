import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA = x
    catB = y
    mouseC = z

    dist1 = abs(catA - mouseC)
    dist2 = abs(catB - mouseC)

    if (dist1 == dist2):
        return('Mouse C')
    elif (dist1 > dist2):
        return('Cat B')
    else:
        return('Cat A')


x = 1
y = 3
z = 2
result = catAndMouse(x, y, z)
print(result)