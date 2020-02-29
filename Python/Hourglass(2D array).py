'''Given a 6x6 2D Array, arr :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values
with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in arr, and an hourglass sum
is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in arr,
then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
We calculate the following  hourglass values:

-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
Our highest hourglass value is '28' from the hourglass:

0 4 3
  1
8 6 6


hourglassSum has the following parameter(s):

arr: an array of integers
Input Format
Each of the  lines of inputs  contains  space-separated integers .

Output Format
Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19'''



# Solution:

R=6
C=6
m=[]
sum=0
l=[]

# This loop is for 2d-Matrix Input with space seperated integers.

for _ in range(6):
    m.append(list(map(int, input().rstrip().split())))

#print(m)        

for i in range(4): # 4 here is problem specific. use R-2 for general cases.
    for j in range(4): # 4 here is problem specific. use C-2 for general cases.
        sum=m[i][j]+m[i][j+1]+m[i][j+2]+m[i+1][j+1]+m[i+2][j]+m[i+2][j+1]+m[i+2][j+2]
        l.append(sum)
print(max(l))        
        
        
# OUTPUT:

''' RESTART: C:/Users/aditya/Desktop/python beginning/Hackerank Python/Hourglass(2D array).py 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
19
>>>''' 


























