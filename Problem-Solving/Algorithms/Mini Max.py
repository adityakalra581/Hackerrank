a = [1,2,3,4,5]

## Min Max Algorithm:

# Identifying Minimum and Maximum sum with 4 out 5 elements in this array.

# That means find an combination of 4 numbers that gives maximum sum and Minimum sum

def minimax(a):
    print(sum(a)-max(a),sum(a)-min(a))

minimax(a)

## OUTPUT:

# 10 14

## Minimum = Total Sum - Minimum value in the Array.

## Maximum = Total Sum - Maximum value in the Array.