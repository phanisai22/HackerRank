class Person:
    def __init__(self, first_name, last_name, id_number):
        self.firstName = first_name
        self.lastName = last_name
        self.idNumber = id_number

    def print_person(self):
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

    scores = 0

    def __init__(self, first_name, last_name, id_number, score):
        super().__init__(first_name, last_name, id_number)
        self.scores = score

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    @property
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        grade = ''
        if 90 <= avg <= 100:
            grade = 'O'
        elif 80 <= avg < 90:
            grade = 'E'
        elif 70 <= avg < 80:
            grade = 'A'
        elif 55 <= avg < 70:
            grade = 'P'
        elif 40 <= avg < 55:
            grade = 'D'
        elif avg < 40:
            grade = 'T'
        return grade


line = input().split()
first_name = line[0]
last_name = line[1]
id_num = line[2]
numScores = int(input())  # not needed for Python
score = list(map(int, input().split()))
s = Student(first_name, last_name, id_num, score)
s.print_person()
print("Grade:", s.calculate)
