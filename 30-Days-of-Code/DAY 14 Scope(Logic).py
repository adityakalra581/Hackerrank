


## BASIC LOGIC BEHIND DAY 14 SCOPE TASK.
## TO FIND THE MAXIMUM ABSOLUTE DIFFERENCE BETWEEN THE ELEMENTS IN THE LISTS.


a=[1,2,4,5,7,19,88,100,23]
min=101
## Assigned as given in the question
max=0
## given
## As the range of elemets is between 1 and 100.
max_diff=0
for i in a:
    if i<min:
# if the current element is less than the minimum element
# Then assign it minimum
        min=i
    if i>max:
# if the current element is greater than the maximum element
# Then assign it maximum
        max=i

## Maximum absolute difference.
max_diff=max-min
print(max_diff)
        
