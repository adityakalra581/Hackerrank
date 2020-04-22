# TASK : Random Clock timing ,convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 
# 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45
 
# ***************************************************************** 


# s = "01:34:50AM"     ## Test Case 1
s = "12:45:54PM"       ## Test Case 2
x = 0
y = 0
# print(x*10 + y*1 + 12,a[2::])

def timeConversion(s):
    #
    # Write your code here.
    #
    x = 0
    y = 0
    if s[8]=="P":
        x = int(s[0])
        y = int(s[1])
        h = x*10 +y*1
        if h==12:
            ans = str(x*10 + y*1) + s[2:8]
        else:
            ans = str(x*10 + y*1 + 12) + s[2:8]
    else:
        x = int(s[0])
        y = int(s[1])
        h = x*10 +y*1
        if h==12:
           ans = str(x*10 + y*1 - 12)+ "0" + s[2:8]
        else: 
            ans = s[:8]
    return ans

print(timeConversion(s))
