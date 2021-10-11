import datetime


def bot():
    name = input("Hi, may i know your name please? ")
    print(f"Welcome {name}, how may I help you?")
    request = input("")
    if "results" or "result" or "cgpa" in request:
        print("Submit your details")
        cgpa()
    else:
        print("I cannot process your requests! Goodbye🖐🖐")


def cgpa():
    # CGPA = 0  # cumulative grade point average
    # GP = 0  # grade point
    CP = 0  # credit point
    TCP = 0  # total credit point
    GPA = 0  # grade point average
    TLU = 0  # sum of credit unit
    grades = """"""

    # course_count = 1
    course_count = int(input("Enter the number of courses you are offering: "))
    course_count += 1

    stud_course_info1 = []

    while course_count > 0:
        # stud_course_info1.append(course_count)
        course_count -= 1

        while course_count > 0:
            course_name = ""
            course_unit = ""
            course_grade = ""

            stud_course_info2 = [course_name, course_unit, course_grade]
            course_name = input("Enter course name: ")
            course_unit = int(input("Enter course unit: "))
            course_grade = int(input("Enter your score: "))
            if course_grade <= 44:
                grades += f"You have F in {course_name}\n"
            elif course_grade <= 49:
                grades += f"You have D in {course_name}\n"
            elif course_grade <= 59:
                grades += f"You have C in {course_name}\n"
            elif course_grade <= 69:
                grades += f"You have B in {course_name}\n"
            elif course_grade <= 100:
                grades += f"You have A in {course_name}\n"
            else:
                print("Invalid input! Enter a value between 0 - 100")
            stud_course_info2[0] = course_name
            stud_course_info2[1] = course_unit
            TLU += course_unit
            stud_course_info2[2] = course_grade

            if course_grade <= 44:
                CP = course_unit * 0
            elif course_grade <= 49:
                CP = course_unit * 2
            elif course_grade <= 59:
                CP = course_unit * 3
            elif course_grade <= 69:
                CP = course_unit * 4
            elif course_grade <= 100:
                CP = course_unit * 5
            else:
                print("Invalid input! Enter a value between 0 - 100")

            TCP += CP

            GPA = TCP / TLU

            stud_course_info1.append(stud_course_info2)
            course_count -= 1

    print(stud_course_info1)
    # print(TCP)
    # print(TLU)
    print(f"Below are your grades:\n {grades}")
    print(f"Your GP is {GPA}")

    if GPA <= 2.39:
        print("You are on Third Class")
    elif GPA <= 3.49:
        print("You are on Second Class Lower")
    elif GPA <= 4.49:
        print("You are on Second Class Upper")
    elif GPA <= 5.00:
        print("You are on First Class")
    else:
        print("Invalid, Your details is out of range.")

    db = open("results.txt", "w+")
    x = str(datetime.datetime.now())

    db.write(f"{x}\n")
    db.write(grades)
    db.write(f"Your GP is {GPA}")
    db.close()


bot()
