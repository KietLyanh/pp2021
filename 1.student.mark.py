
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


