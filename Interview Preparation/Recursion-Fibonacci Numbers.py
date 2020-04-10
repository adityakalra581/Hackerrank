## Recursion: Fibonacci Numbers

##Input Format

"""
The input line contains a single integer, .

Output Format:

prints the integer value returned by the  function.
"""

### FIBONACCI SERIES:

## 0,1,1,2,3,5,8,13,21,34,55.....



def fibonacci(n):

    # Write your code here.
    if n<= 0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

n = int(input())
print(fibonacci(n))


"""
Input : 12
Output : 144

Input : 9
Output : 34
"""
