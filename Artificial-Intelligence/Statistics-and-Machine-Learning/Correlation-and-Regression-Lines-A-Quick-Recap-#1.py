########

# Calculating Pearson correlation of coefficient:
# without any library.







# Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy as np
# from scipy.stats import pearsonr


import math

l1=[15,12,8,8,7,7,7,6,5,3]

l2=[10,25,17,11,13,17,20,13,9,15]

# corr, _ = pearsonr(l1, l2)
# print('Pearsons correlation: %.3f' % corr)

## Formula of Pearson Correlation coefficient:
## r = Summation(x,y)/(summ(x^2)*summ(y^2))^0.5
## Here x=l1-mean(l1) and y=l2-mean(l2)


## Mean of column 1 and 2:
m1 = sum(l1)/len(l1)
m2 = sum(l2)/len(l2)

# print(m1)      # = 7.8
# print(m2)      # = 15

x=[ i - m1 for i in l1 ]
y = [ j - m2 for j in l2 ]

#print(x)
#print(y)

xy = [x[i]*y[i] for i in range(len(l1))]

num = sum(xy)
#print(s)


g=sum([i**2 for i in x ])
h=sum([i**2 for i in y ])
# print(g)
# print(h)

den = math.sqrt(h*g)

r=num/den
#print(r)
print(round(r,3))
