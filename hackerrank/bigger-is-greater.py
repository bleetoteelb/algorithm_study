#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    wl = list(w)
    k,i,n = -1,-1,len(wl)
    j = 0
    for j in range(n-1):
        if ord(wl[j])<ord(wl[j+1]):
            k,i = j,j+1
    if k==-1:
        return "no answer"

    for j in range(k+1,n):
        if ord(wl[k])<ord(wl[j]):
            i = j

    wl[k], wl[i] = wl[i], wl[k]
    answer = wl[:k+1] + list(reversed(wl[k+1:]))

    return ''.join(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

