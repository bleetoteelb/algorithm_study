#!/bin/python3

import math
import os
import random
import re
import sys
import itertools 

# Complete the encryption function below.
def encryption(s):
    size = len(s)
    N = int(math.sqrt(size))
    N = N if N*N==size else N+1
    splited = [ s[i*N:(i+1)*N] for i in range(N) ]
    answer = []
    for i in itertools.zip_longest((*splited),fillvalue=''):
        answer.append(''.join(i))
    return ' '.join(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

