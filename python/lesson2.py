#Variables in Python
student_name = "John" #String
second_name = "Doe" #String
student_age = 25 #Integer
student_height =  1.78 #Float
student_admitted = True #boolean

#Operators in Python
#1. Arithmetic operators
num1 = 10
num2 = 20
addition = num1 + num2
#print(addition)
subtraction = num1 - num2
#print(subtraction)
print(num1 == num2)
print(num1 != num2)
#6. Conditional statements
#if,elif,else

if student_age >= 18:
    print ("You are an adult")

    enter_name = input ("Enter your name")
    enter_age = int (input("Enter your age:"))
    if enter_age >= 18:
        print(enter_name , "is an adult")