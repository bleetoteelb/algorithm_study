#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

