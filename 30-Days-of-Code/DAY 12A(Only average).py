# problem Link: https://www.hackerrank.com/challenges/30-inheritance/problem

## BASIC LOGIC BEHIND THE PROBLEM:

## Actual Task:
## Taing scores in a single line, summing them and finding avg.
# The according to the average provide Grades.


n=int(input())
x=[]
#for i in range(n):
x=list(map(int,input().split()))


print(x)
#avg=(sum(x))/n


def calculate(x):
    avg=(sum(x))/n
    if 90<=avg<=100:
       print("Grade: O")
    elif 80<=avg<90:
       print("Grade: E")
    elif 70<=avg<80:
       print("Grade: A")
    elif 70<=avg<80:
       print("Grade: A")
    elif 55<=avg<70:
       print("Grade: P")
    elif 40<=avg<55:
       print("Grade: D")
    else:
       print("Grade: T")

calculate(x)
