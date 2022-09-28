import math
import os
import random
import re
import sys

def countSwaps(a):
    sw=0
    n=len(a)
    for i in range(n): 
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1]= a[j+1],a[j]
                sw +=1 
            else:
                a[j],a[j+1] =a[j],a[j+1]
                sw=sw
    print("Array is sorted in"+ " "+str(sw)+" "+"swaps.")
    print("First Element:" +" " +str( a[0] )) 
    print("Last Element:" + " "+str(a[n-1] ))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)