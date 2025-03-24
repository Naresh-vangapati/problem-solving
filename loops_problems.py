# 1. Print all numbers from 1 to 100 using a for loop

# for num in range(1,101):
#     print(num)

# 2.Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)

# n = int(input("Enter a number : "))
# sum=0
# for num in range(1,n+1):
#     print(num)
#     sum = sum + num
# print(sum)

# print((n*(n+1))/2)

    

# 3. Print all even numbers between 1 and 50 using a while
# loop.

# num = 2 
# while num < 51:
#     print(num)
#     num += 2 


# 4.Write a program to display the multiplication table of a given
# number. First 20

# num = int(input("Enter a number : "))
# count = 0 
# while count<11:
#     table = num * count
#     count=count+1
#     print(f"{num} * {count} = {table}")

    


# 5.Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.


# num1 = int(input("Enter a number : "))
# dig_sum = 0
# rev_num = 0
# while num1>0:
#     rem = num1%10
#     dig_sum+=rem
#     rev_num = rev_num*10 + rem
#     num1 = num1//10
# print(dig_sum)
# print(rev_num)

# 6.Write a program to count the number of digits in a given
# number using a while loop.


# num = int(input("Enter a number : "))
# count=0
# while num>0:
#     rem = num%10
#     count+=1
#     num = num//10
# print(count)

# 7. Write a program that keeps asking the user to enter numbers
# until they enter a negative number. Use a while loop.


# while True:
#     num = int(input("Enter a non negative number : "))
#     if num<0:
#         break

# num = int(input("Enter a non negative number : "))
# while num >= 0 :
#     num = int(input("Enter a non negative number : "))


# MEDIUM QUESTIONS:-

# 1.Print the first 10 terms of the Fibonacci series using a for
# loop

# input=int(input("enter the range : "))
# first=0
# second=1
# for i in range(input):
#     print(first)
#     temp=first+second
#     first=second
#     second=temp

# 2.Check if a given number is a prime number using a for
# loop

# prime_input=int(input("enter number : "))
# if prime_input>1:
#     for i in range(2,(prime_input//2)+1):
#         if prime_input % i == 0:
#             print("Not a prime")
#             break
#     else:
#         print("Prime Number")
            
# else:
#     print("Not a prime")


# 3. Write a program to calculate the factorial of a number using
# a while loop

# num = int(input("Enter a non negative number : "))
# factorial = 1
# while num>0:
#     factorial = factorial * num
#     num -=1   
# print(factorial)



# 4.Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop

# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print(i)



# 5.Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit

# num = int(input("Enter a number : "))
# while True:
#     if num==1:
#         num1 = int(input("Enter a number for square : "))
#         square = num1 * num1
#         print("square of the given number is",square)
#         break
#     elif num ==2:
#         num2 = int(input("Enter a number for cube : "))
#         cube = num2 * num2 * num2 
#         print("cube of the given number is",cube)
#         break
#     elif num == 3:
#         print("Exit")
#         break
#     else:
#         print ("Enter a valid number 1 or 2 or 3")
#         break




# 6.Implement a basic login system where the user has three
# attempts to enter the correct password using a loop

# attempts = 3
# EmailId = "login@gmail.com"
# Password = "1234"
# while attempts>0:
#     Email_Id = input("enter a EmailId:")
#     Pass_word = input("enter a Password:")
#     if EmailId == Email_Id and Password == Pass_word:
#         print("login successfull")
#         break
#     attempts -= 1 
#     if attempts == 0:
#         print("Login failed! No attempts left, Please try again later.")
#     else:
#         print(f"still you have {attempts} attemps")
