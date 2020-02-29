
# https://www.hackerrank.com/challenges/predicting-office-space-price/problem
## Polynomial Regression: Office Prices


## Simply put:
# 2 independent variables and one dependent variable provided.
# Create a model and predict the dependent variable.
# Simple multiple regression problem.
# With a twist:
# data will be given as input and not in csv structured format.

"""
Input Format

The first line contains two space separated integers, F and N.
Over here, F is the number of observed features. N is the number of rows for which
features as well as price per square-foot have been noted.

This is followed by a table having F+1 columns and N rows with each row in a new
line and each column separated by a single space.
The last column is the price per square foot.

The table is immediately followed by integer T followed by T rows
containing F columns.

2 100
0.44 0.68 511.14
0.99 0.23 717.1
0.84 0.29 607.91
0.28 0.45 270.4
0.07 0.83 289.88
0.66 0.8 830.85
0.73 0.92 1038.09
......
..... and so on.


Test data:

4
0.05 0.54
0.91 0.91
0.31 0.76
0.51 0.31

Need to predict the Third column for this data.

"""





from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Set data
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
lr = LinearRegression()
lr.fit(poly.fit_transform(np.array(X)), Y)

# Get the parameters X for discovery the Y
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = lr.predict(poly.fit_transform(np.array(new_X)))
for i in range(len(result)):
    print(round(result[i],2))
