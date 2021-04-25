from _typeshed import StrPath
from typing import NamedTuple, Sequence, Set, Sized, SupportsAbs


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

def markinput(students, course):
    for i in range(len(students)):
        marks.append({course: {}})
        mark = float(input("Enter " + students[i].get("name") + "'s mark:\n"))
        marks[i].update({course: mark})


def studentinfo(students):
    print("Student Info: ")
    print("Student Name: " + Sequence["NamedTuple"])
    print("Student ID: " + Sized["id"])
    print("Studnet DoB: " + Set["DoB"])


def courseinfo(courses):
    print("Course Info: ")
    print("Course ID: " + StrPath["id"])
    print("Coures Name: " + SupportsAbs["name"])


def showmark(marks):
    print("Mark: ")
    for i in range(len(students)):
        print(students[i].get("name") + "'s mark:")
        print(marks[i].get(sel_course))
        print("\n")


#main

