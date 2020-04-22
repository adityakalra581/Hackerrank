# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

a = [[11,2,4],
     [4,5,6],
     [10,8,-12]]


## LEFT DIAGONAL:

## 11,5,-12

## RIGHT DIAGONAL:

## 4,5,10


n = len(a)
# print(n)

d1 = 0
d2 = 0
for i in range(n):
    for j in range(n):
        if i==j:
            d1 += a[i][j]
        if i+j==n-1:
            d2 += a[i][j]



print("Sum of left Diagonal",d1)
print("Sum of right diagonal",d2)
print("Absolute difference of both the Diagonals",abs(d1-d2))


# OUTPUT:

# Sum of left Diagonal 4
# Sum of right diagonal 19
# Absolute difference of both the Diagonals 15

# *******************************************************