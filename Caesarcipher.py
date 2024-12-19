#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Normalize the shift to be within the range [0, 25]
    k = k % 26
    result = []

    for char in s:
        if 'a' <= char <= 'z':  # For lowercase letters
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':  # For uppercase letters
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(new_char)
        else:  # Non-alphabetic characters
            result.append(char)

    return ''.join(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
