import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def countingSort(arr):
    # Write your code here
    list2=[]
    list= [0]*len(arr)
    for j in range(len(arr)):
        list[arr[j]] +=1
    if len(list)<=100:
        return list
    else:
        for i in range(len(list)):
            if list[i] !=0:
                list2.append(list[i])
            
        return list2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()