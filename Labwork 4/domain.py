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