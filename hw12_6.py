class Course:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.credits=[]

    def add_course(self, course, credit):
        self.courses.append(course)
        self.credits.append(credit)

class Student:
    def __init__(self, name, studentNum):
        self.name = name
        self.studentNum = studentNum
        self.departments = []
        self.courses = []

    def add_department(self, department):
        self.departments.append(department)

    def enroll(self, course):
        self.courses.append(course)



dept=Department("컴퓨터")
math1=dept.add_course("공업수학", 3)
math2=dept.add_course("이산수학", 2)

kim=Student("Kim", 20200001)
kim.enroll(math1)