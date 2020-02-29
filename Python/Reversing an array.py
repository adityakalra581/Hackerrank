'''An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  (you may also see it written as ).

Given an array,A, of N integers, print each element in reverse order as a single line of space-separated integers.


Input Format

The first line contains an integer, N (the number of integers in A ).
The second line contains N space-separated integers .


Output Format

Print all  integers in  in reverse order as a single line of space-separated integers.

Sample Input 1
 
4
1 4 3 2
Sample Output 1

2 3 4 1

'''
# SOLUTION:

def Reverse(lst): 
    arr.reverse() 
    return arr
# In built function for reversing an array.

arr_count = int(input())

arr = list(map(int, input().rstrip().split()))
# Taking input for array after giving space after every input


#print(Reverse(arr))
y=Reverse(arr)


# The below code is for removing the parenthesis.
# It is not neccesary but problem specific.

print( " ".join( repr(e) for e in y ) )
# In between the " " we can add anything to seperate the integers.
