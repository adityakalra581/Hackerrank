
# PROBLEM LINK:
# https://www.hackerrank.com/challenges/python-lists/problem
# REFER THE LINK FOR FULL PROBLEM EXPLANATION.

'''Consider a list (list = []). You can perform the following commands:

insert 
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

n=int(input())
l=[]
for i in range(n):
    h=[]
    h.append(input().split())
       
    if h[0][0]=='insert': 
        m=int(h[0][1])
        a=int(h[0][2])
        l.insert(m,a)
    elif h[0][0]=='print':
        print(l)
    elif h[0][0]=='remove':
        m=int(h[0][1])
        l.remove(m)
    elif h[0][0]=='append':
        m=int(h[0][1])
        l.append(m)
    elif h[0][0]=='sort':
        l.sort()
    elif h[0][0]=='pop':
        l.pop()
    elif h[0][0]=='reverse':
        l.reverse()

         
