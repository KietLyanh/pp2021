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