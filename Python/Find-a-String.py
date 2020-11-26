### Finding the frequency of a sub-string in a bigger string.

## Problem Link: https://www.hackerrank.com/challenges/find-a-string/problem
## Solution Credits: https://www.geeksforgeeks.org/frequency-substring-string/


def count(sub_string, string):
    s = len(string)
    sub_s = len(sub_string)
    count = 0

    for i in range(s - sub_s + 1):
        j = 0

        while j < sub_s:
            if string[i+j] != sub_string[j]:
                break
            j +=1

        if j == sub_s:
            count += 1
            j = 0
    return count, string, sub_string

## Driver Code:
if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    print(count(sub_string, string))
