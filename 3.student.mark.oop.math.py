import math
import numpy as np

class Student:
    def __init__(self, ID, name, DoB):
        self.ID = ID
        self.name = name
        self.DoB = DoB

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_DoB(self):
        return self.DoB

    def setID(self, ID):
        self.ID = ID

    def setname(self, name):
        self.name = name

    def getGPA(self):
        return (float)(self.GPA)

    def setDoB(self, DoB):
        self.DoB = DoB

    def __eq__(self, other):
        return self.ID == other.ID

    def get_key(self):
        return self.get_ID()

    def displayStudentInformation(self):
        print("Student Id: %d, Student name: %s, Student dob: %s" % (self.ID, self.name, self.DoB))


class Course:
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName

    def get_course_ID(self):
        return self.courseID

    def get_course_name(self):
        return self.courseName

    def set_course_name(self, courseName):
        self.courseName = courseName

    def set_course_ID(self, courseID):
        self.courseID = courseID

    def __eq__(self, other):
        return self.courseID == other.courseID

    def get_key(self):
        return self.get_course_ID()

    def displayCourseInformation(self):
        print("CourseID: {}, Course name: {}".format(self.courseID, self.courseName))


class Mark:
    def __init__(self, studentID, courseID, grade):
        self.studentID = studentID
        self.courseID = courseID
        self.grade = grade

    def get_student_ID(self):
        return self.studentID

    def get_course_ID(self):
        return self.courseID

    def get_grade(self):
        return self.grade

    def set_student_ID(self, studentID):
        self.studentID = studentID

    def set_course_ID(self, courseID):
        self.courseID = courseID

    def set_grade(self, grade):
        self.grade = grade

    def __eq__(self, other):
        return self.get_student_ID() == other.get_student_ID() and self.get_course_ID() == other.get_course_ID()

    def displayStudentMark(self, studentName):
        print("Student Id: {}, Student Name: {}, Student Mark: {} ".format(self.studentID, studentName, self.grade))




students = []
courses = []
marks = []


def inputstudentsinaclass():
    numberstudentsinaclass = int(input("Input number of students in a class: "))
    return numberstudentsinaclass


def inputstudentinformation():
    studentID = input("Input student ID: ")
    studentName = input("Input student name: ")
    studentDoB = input("Input student DoB: ")
    studentsinfo = {"Student ID": studentID, "Student Name": studentName, "Student DoB": studentDoB}
    return studentsinfo


def inputnumberofcourses():
    numberofcourses = int(input("Input the number of courses: "))
    return numberofcourses


def inputcourseinformation():
    courseID = input("Input course ID: ")
    coursename = input("Input course name: ")
    coursesinfo = {"Course ID": courseID, "Course Name": coursename}
    return coursesinfo 

def CourseMarkIntroduction():
    print("Enter the mark about the course")
    numberofstudent = int(input("Number of student in the course:"))
    return numberofstudent

def markinput():
    print("Enter the mark of each student")
    mark = input("Mark:")
    markinfo = {"Student Mark": mark}
    return markinfo


def studentinfo(students):
    print('Student Info:')
    for key in studentsinfo:
        print(key, ':', studentsinfo[key])



def courseinfo(courses):
    print('Course Info:')
    for key in coursesinfo:
        print(key, ':', coursesinfo[key])

def showmark(marks):
    print("Mark")
    for key in markinfo:
        print(key, ':', markinfo[key])

def calculateGPA(student):
    ttCredis = 0
    ttMarks = 0
    for course in student.CoursesList:
        ttMarks = ttMarks + course.Mark * course.Credit
        ttCredis = ttCredis + course.Credit
    if ttCredis == 0:
        gpa = 0
    else:    
        gpa = ttMarks/ttCredis
    student.GPA = round(gpa)


#main

print("Welcome to student mark management program")
print("First you need to enter number of student: ")
numberofstudents = inputstudentsinaclass()
for x in range (0, numberofstudents):
    studentsinfo = inputstudentinformation()
    students += studentsinfo
print("Second, you need to enter number of course: ")
numberofcourses = inputnumberofcourses()
for y in range (0, numberofcourses):
    coursesinfo = inputcourseinformation()
    courses += coursesinfo
studentmark = CourseMarkIntroduction()
for z in range (0, studentmark):
    markinfo = markinput()
    marks += markinfo

print("What do you want to do")
print("1. See course information")
print("2. See student information")
print("3. See student mark")
print("4. Add student")
print("5. Add course")
print("6. Input Mark")
options = int(input("Choose option: "))

if options == 1:
    courseinfo(courses)
elif options == 2:
    studentinfo(students)
elif options == 3:
    showmark(marks)
elif options == 4:
    inputstudentinformation()
elif options == 5:
    inputcourseinformation()
elif options == 6:
    markinput()
else:
    print("Error")

print("Do you want to something else? Yes/No")
somethingelse = input("Do you want to something else?")
if somethingelse == ("Yes"):
    print("1. See course information")
    print("2. See student information")
    print("3. See student mark")
    print("4. Add student")
    print("5. Add course")
    print("6. Input Mark")
    options2 = int(input("Choose option: "))

    if options == 1:
        courseinfo(courses)
    elif options == 2:
        studentinfo(students)
    elif options == 3:
        showmark(marks)
    elif options == 4:
        inputstudentinformation()
    elif options == 5:
        inputcourseinformation()
    elif options == 6:
        markinput()
    else:
        print("Error")
else:
    print("Shutdown")



