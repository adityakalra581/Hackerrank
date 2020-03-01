

import math
n=int(input())
for j in range(n):
    x=int(input())
    m=math.floor(math.sqrt(x))
    if n>1:
        for i in range(2,m):
            if x%i==0:
                print("Not prime")               
            else:
                print("Prime") 
   
