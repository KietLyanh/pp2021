import math
import numpy
class Student:
    def __init__(self, ID, Name, DoB, GPA):
        self.ID = ID
        self.Name = Name
        self.DoB = DoB

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getDoB(self):
        return self.DoB

    def setID(self, ID):
        self.ID = ID

    def setName(self, Name):
        self.name = Name

    def setDoB(self, DoB):
        self.DoB = DoB

    def getGPA(self):
        return self.GPA

    def setGPA(self, GPA):
        self.GPA = GPA


class Course:
    def __init__(self, courseID, courseName, courseMark):
        self.courseID = courseID
        self.courseName = courseName
        self.courseMark = courseMark

    def getcourseID(self):
        return self.courseID

    def getcoursename(self):
        return self.courseName

    def setcoursename(self, courseName):
        self.courseName = courseName

    def setcourseID(self, courseID):
        self.courseID = courseID

    def setMark(self, students):
        for student in students:
            studentName = students.get_Name()
            mark = input("Enter the mark: ")

    def getcredit(self):
        return self.credit
    
    def setcredit(self, credit):
        self.credit = credit

if __name__ == "_main_":
    students = []
    courses = []

def inputstudentsinaclass():
    numberstudentsinaclass = int(input("Input number of students in a class: "))
    return numberstudentsinaclass


def inputnumberofcourses():
    numberofcourses = int(input("Input the number of courses: "))
    return numberofcourses


def courseinfo(courses):
    print("The courses that the students taking in are:")
    for course in courses:
        print(course.getcoursename())

def addCourse():
    for i in range(inputnumberofcourses()):
        coursename = input("Input course name: ")
        studentID = input("Input student ID: ")
        mark = input("Enter the mark of the students: ")
        credit = input("Enter course credit")
        return courses(Course(coursename, studentID, mark, credit))

def addStudent():
     for i in range(inputstudentsinaclass()):
        studentName = input("Input student name: ")
        studentDoB = input("Input student DoB: ")
        studentID = input("Input student ID: ")
        students.append(Student(studentName, studentDoB, studentID))   

def caculateGPA(self):
        sum_credits = 0
        for i in range(inputnumberofcourses()):
            self.GPA += int(self.mark[1][i]) * int(self.mark[2][i])
            sum_credits += int(self.mark[2][i])

        self.GPA = math.floor((self.gpa/sum_credits) * 10) / 10
        return self.GPA
#main

print("Welcome to student mark management program")
print("What do you want to do")
print("1. Add student")
print("2. Add course")
print("3. Calculate GPA")
options = int(input("Choose option: "))

if options == 1:
    addStudent()
elif options == 2:
    addCourse()
elif options == 3:
    caculateGPA()
else:
    print("Error")