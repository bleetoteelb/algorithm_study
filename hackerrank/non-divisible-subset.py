#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    answer = 0
    cnt = [0 for i in range(k)]
    for i in s:
        cnt[i%k] += 1

    print(cnt)
    for i in range(1,k//2 if k%2==0 else k//2+1):
        answer += max(cnt[i],cnt[k-i])
    if cnt[0]>0:
        answer += 1
    if k%2==0 and cnt[k//2]:
        answer += 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

