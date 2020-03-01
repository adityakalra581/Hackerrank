## INHERITANCE
# problem Link: https://www.hackerrank.com/challenges/30-inheritance/problem






class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)              ## Responsible for inhereting the attributes from parent class.
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg=(sum(self.scores))/n
        if 90<=avg<=100:
            print("Grade: O")
        elif 80<=avg<90:
            print("Grade: E")
        elif 70<=avg<80:
            print("Grade: A")
        elif 70<=avg<80:
            print("Grade: A")
        elif 55<=avg<70:
            print("Grade: P")
        elif 40<=avg<55:
            print("Grade: D")
        else:
            print("Grade: T")
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
n = int(input()) 
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
s.calculate()


## Minute changes to the HackerRank solution.
# Use return inside calculate function instead printing Grades.
# Although both methods are correct.

'''
Input :
Heraldo Memelli 8135627
2
100 80

Output:
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
'''


