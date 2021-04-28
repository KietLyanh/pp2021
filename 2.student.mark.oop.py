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

    def setDoB(self, DoB):
        self.DoB = DoB

    def __eq__(self, other):
        return self.ID == other.ID

    def get_key(self):
        return self.get_ID()


class Course:
    def __init__(self, courseID, courseName, courseMark):
        self.courseID = courseID
        self.courseName = courseName
        self.courseMark = courseMark

    def get_course_ID(self):
        return self.courseID

    def get_course_name(self):
        return self.courseName

    def set_course_name(self, courseName):
        self.courseName = courseName

    def set_course_ID(self, courseID):
        self.courseID = courseID

    def setMark(self, students):
        for student in students:
            studentdName = student.get_name()
            mark = input("Enter the mark:")

    def __eq__(self, other):
        return self.courseID == other.courseID

    def get_key(self):
        return self.get_course_ID()


students = []
courses = []
marks = []


def inputstudentsinaclass():
    numberstudentsinaclass = int(input("Input number of students in a class: "))
    return numberstudentsinaclass


def inputnumberofcourses():
    numberofcourses = int(input("Input the number of courses: "))
    return numberofcourses


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



