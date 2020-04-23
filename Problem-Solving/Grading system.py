def gradingStudents(grades):
    ans = []
    for i in grades:
        if i >= 38:
            if i%5 == 3:
                i += 2
            elif i%5 == 4:
                i += 1
        ans.append(i)
    return ans

        

grades = [37,43,65,72,84]

result = gradingStudents(grades)

for i in result:
    print(i)
