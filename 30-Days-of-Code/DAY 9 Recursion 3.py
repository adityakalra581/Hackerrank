## Basic Factorial using Recursion.
## problem link: https://www.hackerrank.com/challenges/30-recursion/problem



def fact(n):
    if n==0:
        return 1    ## The foundation is fact(0) = 1 
    else:
        return n*fact(n-1) ## Every fact(n) = n*fact(n-1)
   

print(fact(5))
        


'''
logic:

Factorial(5) = 5* factorial(4)
Factorial(4) = 4* factorial(3)
Factorial(3) = 3* factorial(2)
Factorial(2) = 2* factorial(1)
Factorial(1) = 1
Factorial(0) = 1

'''
