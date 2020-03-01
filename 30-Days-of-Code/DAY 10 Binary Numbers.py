
## Problem Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem


n=int(input())
x=bin(n)
y=x[2::]




#print(y)

# .split('0') will split the consecutive ones from a zero.
#print(y.split("0"))

# we need the maximum length not the maximum value.
# therefore map will maps the length and max will provide us
# the maximum length.
# Map is used as max won't take 2 parameters.


print(max(map(len,y.split("0"))))   ## Maximum length of consecutive ones.
# Reference: https://www.geeksforgeeks.org/python-map-length-longest-consecutive-1s-binary-representation-given-integer/

'''

INPUT: 22

OUTPUT:

10110  (Value of y)= 22 in binary

['1', '11', '']   (Output of y.split)


2   (Final output)

Explanation:
maximum consecutive ones length is 2. 
  
'''
