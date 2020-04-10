#!/bin/python3
"""
Given an array of integers, sort the array in ascending order using the
Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where numswaps is the number of swaps
that took place.

First Element: firstElement, is the first element in the sorted array.

Last Element: lastElement, is the last element in the sorted array.
"""
import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    c = 0
    x = len(a)
    for i in range(x-1):
        for j in range(x-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                c += 1
    print("Array is sorted in",c,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)


## OUTPUT:

"""
Input 
4
4 2 3 1

Expected Output

Array is sorted in 5 swaps.
First Element: 1
Last Element: 4

"""
