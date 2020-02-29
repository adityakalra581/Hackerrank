
## https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Finding the average
# Multiple values and single key problem.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    c=student_marks[query_name]
    Sum=sum(c)
    h=Sum/len(c)
    print("%.2f" % h)
