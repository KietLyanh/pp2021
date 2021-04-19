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
    return studentID, studentName, studentDoB


def inputnumberofcourses():
    numberofcourses = int(input("Input the number of courses: "))
    return numberofcourses


def inputcourseinformation():
    courseID = input("Input course ID: ")
    coursename = input("Input course name: ")
    return courseID, coursename


