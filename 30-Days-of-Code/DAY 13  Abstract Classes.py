## Problem Link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
## Refer before attempting: https://github.com/adityakalra581/30-Days-of-Code/commit/5968d98f440e6025596393e8dff2b6693011f2bc
from abc import ABCMeta,abstractmethod
class Book(object,metaclass=ABCMeta):
    ## We can just import ABC instead of ABCMeta and use it as metaclass.
    # That will also work fine.
    def __init__(self,title,author):
        self.title=title
        self.author=author
        @abstractmethod
        #Just indicating that display is an abstract method. Not important(Can be ignored)
        # Abstract Method: Intstantiation is done here but no implemetation.
        def display(self):
            pass


class MyBook(Book):
## Child Class inhereting from Parent Abstract class.

    
    def __init__(self,title,author,price):
        # super().__init__(self,title,author)  # super(). not working here in abstract classes. 
        Book.__init__(self,title,author)
        self.price=price
    def display(self):
        ## Implemetation is done here for Abstract method.
        
        print("Title : ",self.title)
        print("Author : ",self.author)
        print("Price :",self.price)

title=input()
author=input()
price=int(input())
new = MyBook(title,author,price)
new.display()

'''
INPUT:

The Alchemist
Paulo Coelho
248

OUTPUT:

Title :  The Alchemist
Author :  Paulo Coelho
Price : 248
'''
