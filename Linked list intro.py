'''Input Format

The first line of input contains n, the number of elements in the linked list.
The next n lines contain one element each, which are the elements of the linked list.


Sample Input

2
16
13
Sample Output

16
13
Explanation

There are two elements in the linked list.
They are represented as 16 -> 13 -> NULL.
So, the printLinkedList function should print 16 and 13 each in a new line.
'''


class LinkedList:
    class Node:

        __slots__ = 'element','next'

        def __init__(self,element,next):
            self.element= element
            self.next= next

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0
        
    def addlast(self,e):
        new = self.Node(e,None)
        if self.is_empty():
            self.head=new
            self.tail=new
        else:
            self.tail.next = new
        self.tail=new
        self.size +=1

    def display(self):
        temp=self.head
        while temp:
            print(temp.element,end=' ')
            print()
            temp=temp.next
        print()    
    
N=int(input())
L=LinkedList()

for _ in range(N):
    L_a=int(input())
    L.addlast(L_a)


L.display()

'''
 RESTART: C:/Users/aditya/Desktop/python beginning/Hackerank Python/Linked list intro.py 
INPUT:
4
12
45
78
13
**********************
OUTPUT:
12 
45 
78 
13 
        
        
    
