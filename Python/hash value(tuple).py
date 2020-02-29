'''Task
Given an integer,n , and n space-separated integers as input, create a tuple,t ,
of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not
be imported.

Input Format

The first line contains an integer,n,denoting the number of elements in the
tuple.
The second line contains n space-separated integers describing the elements
in tuple .

Output Format

Print the result of hash(t).

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656  '''

##Python hash()
#The hash() method returns the hash value of an object if it has one.
#Hash values are just integers which are used to compare dictionary keys
#during a dictionary lookup quickly. Internally, hash() method calls
#__hash__()method of an object which are set by default for any object.


n = int(input())
integer_list = tuple(map(int, input().split()))
#tuple() is a constructor for tuples

#print ("The tuple hash value is : " + str(hash(tuple_val))) 
print(str(hash(integer_list)))
