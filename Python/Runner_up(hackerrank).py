#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score. You are given 'n' scores.
#Store them in a list and find the score of the runner-up.

##Input Format:

#The first line contains n. The second line contains an array A[] of n integers each separated by a space.



#Output Format

#Print the runner-up score.






n = int(input())
arr =list(map(int, input().split(" ")))

## split is for spliting a gap between numbers 

y = max(arr)
for i in range(0,n):
    if max(arr) == y:   
        arr.remove(max(arr))
arr.sort(reverse=True)
# Syntax for sorting in descending order



#print(arr)
# This will print an array with max value removed 

print(arr[0])
# runner up element from first array.
