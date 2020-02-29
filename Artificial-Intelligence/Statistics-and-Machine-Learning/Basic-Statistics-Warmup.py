### LINK:https://www.hackerrank.com/challenges/stat-warmup/problem
## Solved every quantity without library except mode:





# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
l.sort()
mean=sum(l)/len(l)
if n%2==0:
    mid1=int(n/2)-1
    mid2=mid1+1
    median=(l[mid1]+l[mid2])/2
else:
    mid=int(n/2)
    median=l[mid]
print(mean)
print(median)

## ******************************
## only quantity i don't know how to calculate without libraries.
from scipy import stats
mode = int(stats.mode(l)[0])
print(mode)
## **************************************
## Standard deviation: Whole_Underroot{(SUMMATION[(x-mean)^2]/n)}

x = [i-mean for i in l]
y = sum([i**2 for i in x])
stdev = (y/n)**0.5
print(round(stdev,1)) 

## Confidence Interval = mean +- t*(sum/(n)^0.5)
## 1.96 t value given in the question..
stderr = stdev/(n**0.5)  ## Know as Standard error.
#print(stderr)
## Margin error = t* standard_error

upper_ci = mean + (1.96*stderr) ## Upper confidence level
lower_ci = mean - (1.96*stderr) ## lower confidence level
print(round(lower_ci,1),round(upper_ci,1))

"""
Output Format

A total of five lines are required.

Mean (format:0.0) on the first line
Median (format: 0.0) on the second line
Mode(s) (Numerically smallest Integer in case of multiple integers)
Standard Deviation (format:0.0) 
Lower and Upper Boundary of Confidence Interval (format: 0.0)
with a space between them.


## Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

## Sample Output

43900.6
44627.5
4978
30466.9
25017.0 62784.2
Note
Use the constant 1.96 while computing the confidence interval.

"""



