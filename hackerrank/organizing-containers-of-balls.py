#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    size = len(container)
    container_sum = sorted([ sum(i) for i in container ])
    type_sum = sorted([sum(i) for i in zip(*container)])

    for i,j in zip(container_sum,type_sum):
        if i!=j:
            return "Impossible"
    else:
        return "Possible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

