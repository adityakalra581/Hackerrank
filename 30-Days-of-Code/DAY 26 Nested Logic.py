# Enter your code here. Read input from STDIN. Print output to STDOUT

x1=list(map(int,input().split()))   # Actual
x2=list(map(int,input().split()))   #Expected

if x1[2]<x2[2]:
    print(0)
elif x1[2]==x2[2]:
    #Check Month
    if x1[1]<x2[1]:
        print(0)
    elif x1[1]==x2[1]:
        #Check Date:
        if x1[0]<=x2[0]:
            print(0)
        else:
            print(15*(x1[0]-x2[0]))
    else:
        print(500*(x1[1]-x2[1]))
else:
    print(10000)        



 

    
       

 


    
       

 

