## Problem Link: https://www.hackerrank.com/challenges/30-scope/problem


class Difference:
    def __init__(self, a):
        self.__elements = a
        ## SOLUTION BEGINS:
        self.maximumDifference=0

    def computeDifference(self):
        maxelement=0
        minelement=101
        for element in self.__elements:
            if element<minelement:
                minelement=element
            if element>maxelement:
                maxelement=element
        self.maximumDifference=maxelement-minelement            

# End of Difference class
# Solution Ends
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

'''
INPUT:
5
4 5 9 66 12

OUTPUT:

62
'''
