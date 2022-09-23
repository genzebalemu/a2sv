import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    n =len(arr)
    #  key=arr[n-1]
    #  for i in range(1,n)
    key=arr[n-1]
    j= n-2
    while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]=arr[j]
            j=j-1
            for k in range(n):
                print(arr[k],end=" ")
            print()
    arr[j+1]=key
   
    for k in range(n):
        print(arr[k],end=" ")
    print()
         
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)