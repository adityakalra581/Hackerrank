
## PROBLEM LINK: https://www.hackerrank.com/challenges/30-review-loop/problem


n=int(input())

for j in range(n):
    s=input()
    e=[]
    o=[]
    for i in range(len(s)):
        if i%2==0:
            e.append(s[i])
        else:
            o.append(s[i])
    #print((*e),' ',(*o))             ## (*e) will give elements with space therfore .join is used.
    print(''.join(e),''.join(o))           ### OUTPUT OF * STAR METHOD:
                                          ##  H c e  a k r (which will fail the test)
    
    ''' 
Sample Input
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak'''
