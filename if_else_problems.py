# 1.write a program to positive,negative or zero


# num =int(input ("enter a number"))
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("number is negative")
# else:
#     print("number is zero")    

# 2.determine  if a number is odd or even


# num = int(input("enter a number"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")     


# 3.check if a person is eligible to vote


# age = int(input("enter age"))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")  


# 4.write a program to find a greatest of two numbers

# num1=30
# num2=25
# print("num1 is greater") if num1 > num2 else print("num2 is greater") 


# 5.print "pass" if a student gets more than 40 marks ; oterwise print "Fail"


# marks = int(input("enter your marks"))
# print("pass") if marks > 40 else print("Fail")



# 6.write a program to display the day of the week based on a number input

# num = int(input("enter a number"))
# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wedness")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else:
#     print("Invalid day")


# 7.implement a simple calculator to perform addition,subtraction,multiplication and division


# operation = input("enter operation to perform").lower()
# op1 =float(input("enter first number"))
# op2 =float(input("enter second number"))
# if operation == "add" or operation == "+":
#  # if operation in ["add","+"]:
#     print(op1 + op2)
# elif operation == "mul" or operation == "*":  
#     print(op1 * op2)
# elif operation == "sub" or operation == "-":
#     print(op1 - op2)  
# elif operation == "div" or operation == "/":
#     if op2 == 0:
#         print("Division by zero is not possible")
#     else:
#         print(op1/op2)  
# else:
#     print("Invalid operation")                  


# 8.write a program to display the name of the month  based on the month based on the mont number        

# month = int(input("Enter a number for month : "))

# if month == 1 :
#     print('January')
# elif month == 2 :
#     print('February')
# elif month == 3 :
#     print('March')
# elif month == 4 :
#     print('April')
# elif month == 5 :
#     print('May')
# elif month == 6 :
#     print('June')
# elif month == 7 :
#     print('July')
# elif month == 8 :
#     print('August')
# elif month == 9 :
#     print('September')
# elif month == 10 :
#     print('October')
# elif month == 11 :
#     print('November')
# elif month == 12 :
#     print('December')
# else:
#     print('invalid month')

# MEDIUM LEVEL QUETIONS

# 1. Write a program to find the greatest of three numbers


# n1=1
# n2=2
# n3=3
# print("n1 is greater") if n1>n2 and n1>n3 else print("n2 is greater") if n2>n1 and n2>n3 else print("n3 is greater")

# 2. Write a program to classify a character entered by the user as a vowel, consonant, or neither.


# n="p"
# if n in ["a", "e", "i", "o", "u"]:
#     print(f"{n} is vowel")
# elif n.isalpha():
#     print(f"{n} is consonant")
# else:
#     print("neither")

#3. Calculate the grade of a student based on the marks they score:
# #     90-100: Grade A
# #     80-89: Grade B
# #     70-79: Grade C
# #     <70: Fail


# marks=8
# if marks>100:
#     print("invalid")
# elif marks<=100 and marks>=90:
#     print("grade A") 
# elif marks<=89 and marks>=80:
#     print("grade B")
# elif marks<=79 and marks>=70:
#     print("grade C")
# elif marks<70:
#     print("Fail")
# else:
#     print("invalid input")


# 4.Check if a year is a leap year. 


# year = int(input("year"))
# if (year%4 == 0 and year%100 != 0) or (year%400==0):
#     print("leap year")
# else:
#     print("not a leap year")


#5. Write a program to check if three sides length form a valid  triangle. 

# side1=float(input("enter the first side"))
# side2=float(input("enter the second side"))
# side3=float(input("enter the thired side"))
# if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
#     print ("triangle can be made")
# else :
#     print ("triangle cannot be made")

