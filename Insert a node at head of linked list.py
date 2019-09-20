# INSERT A NODE AT THE HEAD OF THE LINKED LIST
# AND RETURN THE LINKED LIST IN A REVERSE ORDER:
# EX:
# INPUT:
#        32 23 12
# EXPECTED OUTPUT:
#        12 23 32


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
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#THE PORTION I DID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def insertNodeAtHead(llist, data):
    new = SinglyLinkedListNode(data)
    if llist==None:
        llist=new
        return llist
    else:
        temp=new
        temp.next=llist
        return temp   


## ************************end*********************************    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()
