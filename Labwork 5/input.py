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