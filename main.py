# this program was built to help you process your scores, it other features includes, calculating your GP & CGPA
# this is a revised version
# This is the key to this program
# GP simply means Grade Point
# CU simply means credit unit#
import time

print("===========================WELCOME=================================")
time.sleep(1.5)
print("loading.............. pls wait............")
time.sleep(1)

print("Calculate YOUR GP HERE")
time.sleep(1)
name = input("May I know your name please: ")
time.sleep(1)
print("Hello " + name, " You are welcome here!")
time.sleep(1)
print("I can help you process and compute your results")
time.sleep(1)
print("please enter your grades below")
time.sleep(1)
print("======================================================================")
print("||   Course Name     ||      Scores      ||      Credit Unit        ||")
print("======================================================================")
print("fill in the details of this table")
print("======================================================================")
print("Enter your Courses, Score and Credit Unit")
print("======================================================================")
courseName1 = input("             ")
score1 = int(input("                             "))
CU1 = int(input("                                                            "))
print("======================================================================")
courseName2 = input("             ")
score2 = int(input("                             "))
CU2 = int(input("                                                            "))
print("======================================================================")
courseName3 = input("             ")
score3 = int(input("                             "))
CU3 = int(input("                                                            "))
print("======================================================================")
courseName4 = input("             ")
score4 = int(input("                             "))
CU4 = int(input("                                                            "))
print("======================================================================")
courseName5 = input("             ")
score5 = int(input("                             "))
CU5 = int(input("                                                            "))
print("======================================================================")
courseName6 = input("             ")
score6 = int(input("                             "))
CU6 = int(input("                                                            "))
print("======================================================================")
courseName7 = input("             ")
score7 = int(input("                             "))
CU7 = int(input("                                                            "))
print("======================================================================")
courseName8 = input("             ")
score8 = int(input("                             "))
CU8 = int(input("                                                            "))
print("======================================================================")
courseName9 = input("             ")
score9 = int(input("                             "))
CU9 = int(input("                                                            "))
print("======================================================================")
courseName10 = input("             ")
score10 = int(input("                             "))
CU10 = int(input("                                                            "))
print("======================================================================")
courseName11 = input("             ")
score11 = int(input("                             "))
CU11 = int(input("                                                            "))
print("======================================================================")

F = int(0)
D = int(2)
C = int(3)
B = int(4)
A = int(5)

GP1 = 0
if score1 <= 44:
    GP1 = F * CU1
elif score1 <= 49:
    GP1 = D * CU1
elif score1 <= 59:
    GP1 = C * CU1
elif score1 <= 69:
    GP1 = B * CU1
elif score1 <= 100:
    GP1 = A * CU1

GP2 = 0
if score2 <= 44:
    GP2 = F * CU2
elif score2 <= 49:
    GP2 = D * CU2
elif score2 <= 59:
    GP2 = C * CU2
elif score2 <= 69:
    GP2 = B * CU2
elif score2 <= 100:
    GP2 = A * CU2

GP3 = 0
if score3 <= 44:
    GP3 = F * CU3
elif score3 <= 49:
    GP3 = D * CU3
elif score3 <= 59:
    GP3 = C * CU3
elif score3 <= 69:
    GP3 = B * CU3
elif score3 <= 100:
    GP3 = A * CU3

GP4 = 0
if score4 <= 44:
    GP4 = F * CU4
elif score4 <= 49:
    GP4 = D * CU4
elif score4 <= 59:
    GP4 = C * CU4
elif score4 <= 69:
    GP4 = B * CU4
elif score4 <= 100:
    GP4 = A * CU4

GP5 = 0
if score5 <= 44:
    GP5 = F * CU5
elif score5 <= 49:
    GP5 = D * CU5
elif score5 <= 59:
    GP5 = C * CU5
elif score5 <= 69:
    GP5 = B * CU5
elif score5 <= 100:
    GP5 = A * CU5

GP6 = 0
if score6 <= 44:
    GP6 = F * CU6
elif score6 <= 49:
    GP6 = D * CU6
elif score6 <= 59:
    GP6 = C * CU6
elif score6 <= 69:
    GP6 = B * CU6
elif score6 <= 100:
    GP6 = A * CU6

GP7 = 0
if score7 <= 44:
    GP7 = F * CU7
elif score7 <= 49:
    GP7 = D * CU7
elif score7 <= 59:
    GP7 = C * CU7
elif score7 <= 69:
    GP7 = B * CU7
elif score7 <= 100:
    GP7 = A * CU7

GP8 = 0
if score8 <= 44:
    GP8 = F * CU8
elif score8 <= 49:
    GP8 = D * CU8
elif score8 <= 59:
    GP8 = C * CU8
elif score8 <= 69:
    GP8 = B * CU8
elif score8 <= 100:
    GP8 = A * CU8

GP9 = 0
if score9 <= 44:
    GP9 = F * CU9
elif score9 <= 49:
    GP9 = D * CU9
elif score9 <= 59:
    GP9 = C * CU9
elif score9 <= 69:
    GP9 = B * CU9
elif score9 <= 100:
    GP9 = A * CU9

GP10 = 0
if score10 <= 44:
    GP10 = F * CU10
elif score10 <= 49:
    GP10 = D * CU10
elif score10 <= 59:
    GP10 = C * CU10
elif score10 <= 69:
    GP10 = B * CU10
elif score10 <= 100:
    GP10 = A * CU10

GP11 = 0
if score11 <= 44:
    GP11 = F * CU11
elif score11 <= 49:
    GP11 = D * CU11
elif score11 <= 59:
    GP11 = C * CU11
elif score11 <= 69:
    GP11 = B * CU11
elif score1 <= 100:
    GP11 = A * CU11

GP = GP1 + GP2 + GP3 + GP4 + GP5 + GP6 + GP7 + GP8 + GP9 + GP10 + GP11
CU = CU1 + CU2 + CU3 + CU4 + CU5 + CU6 + CU7 + CU8 + CU9 + CU10 + CU11
GPA = float(GP / CU)

GL = ["Failed, you have F", "Poor, you have D", "Average, you have C", "Good, you have B",
      "Excellent,you got A"]

print("wait " + name + "," + " while I process your inputs..........................")
time.sleep(1.5)
print("loading.............. pls wait............")
time.sleep(1)
print("I am done processing your input...")
time.sleep(1)
print(name + " your result is now ready!")

if score1 <= 44:
    print(GL[0] + " in " + courseName1)
elif score1 <= 49:
    print(GL[1] + " in " + courseName1)
elif score1 <= 59:
    print(GL[2] + " in " + courseName1)
elif score1 <= 69:
    print(GL[3] + " in " + courseName1)
elif score1 <= 1000:
    print(GL[4] + " in " + courseName1)
else:
    print("Invalid Input")
time.sleep(1.5)
if score2 <= 44:
    print(GL[0] + " in " + courseName2)
elif score2 <= 49:
    print(GL[1] + " in " + courseName2)
elif score2 <= 59:
    print(GL[2] + " in " + courseName2)
elif score2 <= 69:
    print(GL[3] + " in " + courseName2)
elif score2 <= 1000:
    print(GL[4] + " in " + courseName2)
else:
    print("Invalid Input")
time.sleep(1.5)
if score3 <= 44:
    print(GL[0] + " in " + courseName3)
elif score3 <= 49:
    print(GL[1] + " in " + courseName3)
elif score3 <= 59:
    print(GL[2] + " in " + courseName3)
elif score3 <= 69:
    print(GL[3] + " in " + courseName3)
elif score3 <= 1000:
    print(GL[4] + " in " + courseName3)
else:
    print("Invalid Input")
time.sleep(1.5)
if score4 <= 44:
    print(GL[0] + " in " + courseName4)
elif score4 <= 49:
    print(GL[1] + " in " + courseName4)
elif score4 <= 59:
    print(GL[2] + " in " + courseName4)
elif score4 <= 69:
    print(GL[3] + " in " + courseName4)
elif score4 <= 1000:
    print(GL[4] + " in " + courseName4)
else:
    print("Invalid Input")
time.sleep(1.5)
if score5 <= 44:
    print(GL[0] + " in " + courseName5)
elif score5 <= 49:
    print(GL[1] + " in " + courseName5)
elif score5 <= 59:
    print(GL[2] + " in " + courseName5)
elif score5 <= 69:
    print(GL[3] + " in " + courseName5)
elif score5 <= 1000:
    print(GL[4] + " in " + courseName5)
else:
    print("Invalid Input")
time.sleep(1.5)
if score6 <= 44:
    print(GL[0] + " in " + courseName6)
elif score6 <= 49:
    print(GL[1] + " in " + courseName6)
elif score6 <= 59:
    print(GL[2] + " in " + courseName6)
elif score6 <= 69:
    print(GL[3] + " in " + courseName6)
elif score6 <= 1000:
    print(GL[4] + " in " + courseName6)
else:
    print("Invalid Input")
time.sleep(1.5)
if score7 <= 44:
    print(GL[0] + " in " + courseName7)
elif score7 <= 49:
    print(GL[1] + " in " + courseName7)
elif score7 <= 59:
    print(GL[2] + " in " + courseName7)
elif score7 <= 69:
    print(GL[3] + " in " + courseName7)
elif score7 <= 1000:
    print(GL[4] + " in " + courseName7)
else:
    print("Invalid Input")
time.sleep(1.5)
if score8 <= 44:
    print(GL[0] + " in " + courseName8)
elif score8 <= 49:
    print(GL[1] + " in " + courseName8)
elif score8 <= 59:
    print(GL[2] + " in " + courseName8)
elif score8 <= 69:
    print(GL[3] + " in " + courseName8)
elif score8 <= 1000:
    print(GL[4] + " in " + courseName8)
else:
    print("Invalid Input")
time.sleep(1.5)
if score9 <= 44:
    print(GL[0] + " in " + courseName9)
elif score9 <= 49:
    print(GL[1] + " in " + courseName9)
elif score9 <= 59:
    print(GL[2] + " in " + courseName9)
elif score9 <= 69:
    print(GL[3] + " in " + courseName9)
elif score9 <= 1000:
    print(GL[4] + " in " + courseName9)
else:
    print("Invalid Input")
time.sleep(1.5)
if score10 <= 44:
    print(GL[0] + " in " + courseName10)
elif score10 <= 49:
    print(GL[1] + " in " + courseName10)
elif score10 <= 59:
    print(GL[2] + " in " + courseName10)
elif score10 <= 69:
    print(GL[3] + " in " + courseName10)
elif score10 <= 1000:
    print(GL[4] + " in " + courseName10)
else:
    print("Invalid Input")
time.sleep(1.5)
if score11 <= 44:
    print(GL[0] + " in " + courseName11)
elif score11 <= 49:
    print(GL[1] + " in " + courseName11)
elif score11 <= 59:
    print(GL[2] + " in " + courseName11)
elif score11 <= 69:
    print(GL[3] + " in " + courseName11)
elif score11 <= 1000:
    print(GL[4] + " in " + courseName11)
else:
    print("Invalid Input")
GPA = str(GPA)
print("Your GPA is " + GPA)
GPA = float(GPA)
if GPA <= 2.39:
    print("Poor, You are on Third Class")
elif GPA <= 3.49:
    print("CREDIT, You are on 2nd Class Lower")
elif GPA <= 4.49:
    print("GOOD, YOU are ON 2nd Class Upper")
elif GPA <= 5.00:
    print("EXCELLENT, ACCEPT MY CONGRATULATIONS, YOU GRADUATED WITH DISTINCTION!")
elif GPA <= 4.00:
    print("")
else:
    print("YOU DON'T HAVE A RESULT, GET OUT!")
time.sleep(15)
print("Thanks for checking your result with us" + ", " + name + "!")
