class Student:
    def __init__(self, ID, Name, DoB):
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
        return courses(Course(coursename, studentID, mark))

def addStudent():
     for i in range(inputstudentsinaclass()):
        studentName = input("Input student name: ")
        studentDoB = input("Input student DoB: ")
        studentID = input("Input student ID: ")
        students.append(Student(studentName, studentDoB, studentID))   
#main

print("Welcome to student mark management program")
print("What do you want to do")
print("1. Add student")
print("2. Add course")
options = int(input("Choose option: "))

if options == 1:
    addStudent()
elif options == 2:
    addCourse()
else:
    print("Error")