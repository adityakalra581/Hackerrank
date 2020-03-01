## Problem link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
## Test cases passed = 4
## Test cases failed = 1
## Issue : RUN TIME ERROR

n=int(input())
phone=dict()
for i in range(n):
    a,b=input().split()
    phone[a]=b

#print(phone)

for i in range (n):
    x=input()
    s=list()
    if x in phone:
        s.append(x)
        s.append(phone[x])
        print('='.join(s))
    else:
        print("Not found")


'''
Input:

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Output:

sam=99912222
Not found
harry=12299933 '''        
