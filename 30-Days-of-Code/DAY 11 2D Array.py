## Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
## Obtaining different sum of hourglass and getting the maximum sum out of it.
## Input is 6x6 matrix.

a=[]
l=[]
sum=[]

for _ in range(6):
    a.append(list(map(int,input().split())))

    
for i in range(4):    ## 4 is problem specific here. For general case use rows-2 
    for j in range(4):  ## 4 is problem specific here. For general case use columns-2 
        sum=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+1]
        l.append(sum)

#print(l)
print(max(l))
        
'''

INPUT:

A 6x6 2D Array.

1 2 4 5 7 8
4 5 6 7 8 9
1 0 0 0 0 0
0 0 0 0 0 0
7 8 9 6 3 2
4 5 6 1 2 3

OUTPUT:

List of sum of hourglass:
l = [13, 17, 23, 28, 15, 18, 21, 24, 24, 26, 21, 12, 22, 26, 14, 8]


Maximum hourglass sum:

28
'''
'''
RANGE = 4 (Explanation)

#Sample Input:

i   j = 0 1 2 3 4 5

0       1 1 1 0 0 0     -> i=0,j=0,1,2,3 if j=4 then there is only one column left to it's right. i and j can go max upto =3.
1       0 1 0 0 0 0     -> thus hourglass will not be complete hence the error.
2       1 1 1 0 0 0     -> similar goes for the i values.
3       0 0 2 4 4 0     -> The maximum value it can compensate is i=3.
4       0 0 0 2 0 0
5       0 0 1 2 4 0 

Similarily now we can do hourglass problem for 8x8 matrix as well.
In that loop will run 6 times and i and j can go upto maximum value of 5.
'''




