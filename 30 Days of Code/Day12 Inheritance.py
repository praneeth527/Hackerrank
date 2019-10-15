class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.scores = scores
        super().__init__(firstName, lastName, idNum)

    def calculate(self):
        self.a = (sum(self.scores) / len(self.scores))
        if (self.a < 40):
            return 'T'
        elif self.a >= 40 and self.a < 55:
            return 'D'
        elif self.a >= 55 and self.a < 70:
            return 'P'
        elif self.a >= 70 and self.a < 80:
            return 'A'
        elif self.a >= 80 and self.a < 90:
            return 'E'
        else:
            return 'O'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
