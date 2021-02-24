#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    answer = []
    setOfRanked = set(ranked)
    listOfRanked = sorted(list(setOfRanked))
    size = len(listOfRanked)
    lastPos = 0
    for ps in player:
        for lsp in range(lastPos, size):
            if ps<listOfRanked[lsp]:
                answer.append(size-lsp+1)
                lastPos = lsp
                break
            elif ps==listOfRanked[lsp]:
                answer.append(size-lsp)
                lastPos = lsp
                break
            elif lsp==size-1:
                answer.append(1)
                lastPos = lsp
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

