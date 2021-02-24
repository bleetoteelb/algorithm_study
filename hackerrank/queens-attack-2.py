#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
# make 4 dirs list will be include filtered obstacles
# 1 -> horizental ------
# 2 -> verticla |
# 3 -> right-up /
# 4 -> right-up \
def queensAttack(n, k, r_q, c_q, obstacles):
    answer = 0
    dir1 = list(filter(lambda x: x[0] == r_q, obstacles))
    dir1.extend([[r_q,0],[r_q,n+1]])
    dir2 = list(filter(lambda x: x[1] == c_q, obstacles))
    dir2.extend([[0,c_q],[n+1,c_q]])
    dir3 = list(filter(lambda x: x[0]-x[1] == r_q-c_q, obstacles))
    if r_q-c_q < 0:
        dir3.extend([[0,c_q-r_q],[n+1-(c_q-r_q),n+1]])
    else:
        dir3.extend([[r_q-c_q,0],[n+1,n+1-(r_q-c_q)]])
    dir4 = list(filter(lambda x: x[0]+x[1] == r_q+c_q, obstacles))
    if r_q+c_q < n:
        dir4.extend([[0,c_q+r_q],[c_q+r_q,0]])
    else:
        dir4.extend([[r_q+c_q-n-1,n+1],[n+1,r_q+c_q-n-1]])

    dir1 = sorted(dir1, key=lambda x:x[1])
    dir2 = sorted(dir2, key=lambda x:x[0])
    dir3 = sorted(dir3, key=lambda x:x[0])
    dir4 = sorted(dir4, key=lambda x:x[0])
    for i in range(len(dir1)):
        if c_q < dir1[i][1]:
            answer += dir1[i][1] - dir1[i-1][1] - 2
            break
    for i in range(len(dir2)):
        if r_q < dir2[i][0]:
            answer += dir2[i][0] - dir2[i-1][0] - 2
            break
    for i in range(len(dir3)):
        if r_q < dir3[i][0]:
            answer += dir3[i][0] - dir3[i-1][0] - 2
            break
    for i in range(len(dir4)):
        if r_q < dir4[i][0]:
            answer += dir4[i][0] - dir4[i-1][0] - 2
            break
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

