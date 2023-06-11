#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    cntmax=cnmin=0
    maxscr=minscr=scores[0]
    for i in range(1,len(scores)):
        if scores[i]>maxscr:
            maxscr=scores[i]
            cntmax+=1
        elif scores[i]<minscr:
            minscr=scores[i]
            cntmin+=1
    return cntmax,cntmin
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
