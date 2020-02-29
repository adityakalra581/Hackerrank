# Insert A node at the tail of the linked list:


## SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
# def addlast(self,e):
        # new = self.Node(e,None)
        # if self.is_empty():
        #     self.head=new
        #     self.tail=new
        # else:
        #     self.tail.next = new
        # self.tail=new
        # self.size +=1


#The Portion i had to do>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def insertNodeAtTail(head, data):
    new = SinglyLinkedListNode(data)
    if head==None:
        head = new
        
    else:
        temp = head
        while temp.next != None:
            temp=temp.next
        temp.next = new
    return head        

## *******************end*************************        


    tail = node

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()




## VIMP: this will run only on hackerrank.    
