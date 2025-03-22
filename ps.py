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


# LOOPS:-



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



# 1.Take input of two numbers from the user and find the LCM of those numbers


# num1=int(input('enter a num1: ')) 
# num2=int(input('enter a num2: ')) 
# greater=max(num1,num2) 
# while True: 
# if greater%num1==0 and greater%num2==0: 
# lcm=greater 
# break 
# greater+=1 
# print(f"lcm of {num1} and {num2} is {lcm}") 



# 2.Take input of two numbers from the user and find the GCD of those numbers 


# num1=int(input('enter a num1: ')) 
# num2=int(input('enter a num2: ')) 
# n1=num1 
# n2=num2 
# while num2!=0: 
# num1,num2=num2,num1%num2 
# print(f"GCD of {n1} and {n2} is: {num1}")


# 3.Print next prime and previous prime of a given number 


# n=29 
# n1=n 
# count=0 
# while count==0: 
#     n=n+1 
#     for i in range (2,n): 
#         fact=0 
#         if n%i==0: 
#             fact+=1 
#             break 
#     if fact==0: 
#         print(n,"is next prime number after",n1) 
#         count=1 


# 4.previous prime number 


# n=29 
# n1=n 
# prev=True 
# while prev: 
#     n=n-1 
#     for i in range (2,n): 
#         fact=0 
#         if n%i==0: 
#             fact+=1 
#             break 
#     if fact==0: 
#         print(n,"is previous prime number before",n1) 
#         prev=False            


# 4.print prime numbers in a given range

# def is_prime(n):
#     """Check if a number is prime."""
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def print_primes_in_range(start, end):
#     """Print all prime numbers in the range [start, end]."""
#     for num in range(start, end + 1):
#         if is_prime(num):
#             print(num)


# 5.write a program to print sum of non-primes in a number

# num1 = int(input("enter a number"))
# def check_prime(input_num):
#     if input_num < 0 or input_num  in [0,1]:
#         return False
#     for i in range(2,input_num):
#         if input_num % 2 == 0:
#             return False
#     return True

# temp = num1 
# non_prime_sum = 0
# while temp > 0:
#     digit = temp % 10
#     if check_prime(digit) == False:
#         non_prime_sum += digit
#     temp = temp // 10   
# print(non_prime_sum)    


# 6. write a program to print sum of odd digits


# num1 = int(input(""))




# 7. armstrong number

# num1 = int(input("enter a number"))
# temp = num1
# temp2 = num1
# sum = 0
# count = 0
# while temp2 > 0:
#     count +=1
#     temp2 = temp2//10

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** count
#     temp = temp // 10
# if sum == num1:
#     print(num1, "is armstrong")
# else:
#     print(num1, "not a armstrong number")      



# 8. write a program to print armstrong nuimbers in the range


# def check_armstrong(input_num): 
#     temp = input_num
#     temp2 = input_num
#     sum = 0
#     count = 0
#     while temp2 > 0:
#         count += 1
#         temp2 = temp2//10

#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** count
#         temp = temp // 10 
#         return sum == input_num  
# num1 = int(input("enter a min number"))
# num2 = int(input("enter a max number"))             
# for i in range(num1, num2+1):
#     if check_armstrong(i):
#         print(i)     



# num1 = int(input("enter a number"))
# def is_palindrome(input_num):
#     temp = input_num
#     rev_num = 0
#     while temp > 0:
#         digit = temp % 10
#         rev_num = rev_num * 10 + digit
#         temp = temp // 10
#     if rev_num == input_num:
#         return True
#     else:
#         return False
        
# print(is_palindrome(num1))



# def num_factorial(input_num):
#     if input_num < 0:
#         print("invalid input")
#         return
#     res = 1
#     for i in range(1, num1 + 1):
#         res *= i
#     return res  
# print(num_factorial(num1)) 



# reverse a list without using inbuilt functions

# list = [1,2.3,True,2,5.5,6,7]
# def reverse_list(input_list):
#     new_list = []
#     for i in input_list:
#         new_list.insert(0,i)
#     return new_list
# list = reverse_list(list)
# print(list)


# def reverse_list_swap(input_list):
#     low =0
#     high = len(list) -1
#     while low < high:
#         input_list[low], input_list[high] = input_list[high], input_list[low]
#         low +=1
#         high -=1
#     return input_list
# list = reverse_list_swap(list)
# print(list)


# def reverse_list_swap(input_list):
#     low = len(input_list)//2
#     high = len(list) -1
#     while low < high:
#         input_list[low], input_list[high] = input_list[high], input_list[low]
#         low +=1
#         high -=1
#     return input_list
# list = reverse_list_swap(list)
# print(list)

# write a program to in a list elements are incresing order or not if it is in increasing order print true else print false

# def check_incresing_order(input_num):
#     temp = input_num
#     pre_digit = 10
#     while temp > 0:
#         digit = temp % 10
#         if digit >= pre_digit:
#             return False
#         pre_digit = digit
#         temp //= 10
#     return True    

# -------------------------------------------------------------------------------------------------------------------------

# def check_incresing_order(input_num):
#     temp = input_num
#     pre_digit = 10
#     while temp > 0:
#         digit = temp % 10
#         if digit > pre_digit:
#             return False
#         pre_digit = digit
#         temp //= 10
#     return True  

# list = [123,231,345,654,789,566,11]
# for i in list:
#     print (check_incresing_order(i))
# ------------------------------------------------------------------------------------------------------------------------

# binary search algorithm

#  list = [1,2,3,4,5,6,7,8,9]
# input = 5
# flag = False

# low = 0
# high = len(list) -1

# while low <= high:
#     mid = (low + high) // 2
#     if list[mid] == input:
#         flag = True
#         print("element found at index", mid)
#         break
#     elif list[mid] > input:
#         high = mid - 1
#     else:
#         low = mid + 1 
# if flag == False:
#     print("element is not found")    
# ----------------------------------------------------------------------------------------------------------------------



# def binary_search(list,input):
#     low = 0
#     high = len(list) -1
#     flag = False
#     while low <= high:
#         mid = (low + high) // 2
#         if list[mid] == input:
#            return mid
#         elif list[mid] > input:
#             high = mid - 1
#         else:
#             low = mid + 1 
#     return -1

# list = [1,2,3,4,5,6,7,8,9]
# print(binary_search(list,input))

# ------------------------------------------------------------------------------------------------------------------------
# bubble sort

# list =[33,5,6,44,9,10,11]
# for j in range(len(list) -1):
#     for i in range(len(list) -1 -j):
#         if list[i] > list[i+1]:
#             list[i] , list[i+1] = list[i+1],list[i]
#     print(list)        




# sum of nested list

# list = [[1,4,5],[5,8,9],[9,5,3]]
# sum = 0
# for i in list:
#     for j in i:
#         sum += j
# print(sum)  
# ------------------------------------------------------------------------------------------------------------------      


# find the minimum and maximum number in nested list

# list = [[1,4,5],[5,8,9],[43,5,30]]
# min_value =list[0][0]
# max_value = list[0][0]
# for i in list:
#     for j in i:
#         if j < min_value:
#             min_value = j
#         elif j > max_value:
#             max_value = j
# print("minimum value in the list is",min_value)
# print("max value in the list is",max_value)           
# -------------------------------------------------------------------------------------------------------------------

# def max_min_missing_num(input_num):
#     list =[]
#     temp = input_num
#     while temp >0:
#         digit = temp % 10
#         list.append(digit)
#         temp //= 10
#     list_min = min(list)
#     list_max = max(list)  
#     for i in range(list_min,list_max+1):
#         if i not in list:
#             print(i)
#     return    
# num =34571     
# max_min_missing_num(num)
# ----------------------------------------------------------------------------------------------------------------------

# list1 = [-4,-2,6,10,12] 
# min_value = list1[0]
# max_value = list1[0]
# for i in list1:
#     if i < min_value:
#         min_value = i
#     elif i > max_value:
#         max_value = i
# list = []        
# for j in range(min_value,max_value +1):
#         if j not in list and j % 2 == 0:
#             print(j)        
# -----------------------------------------------------------------------------------------------------------------------
          

# list1 = [32,24,40,8,6,10,12]
# temp1 = sorted(list1)
# print(list1)
# print(temp1)
# output = []
# for i in list1:
#     res = temp1.index(i) + 1
#     output.append(res)
# print(output)    

# _________________________________________________________________________________________________________________

# list = [-4,-2,22,3,44]
# first_max = float('-inf') 
# for i in list:
#     if i > first_max:
#         first_max = i
# print(first_max)  


# second_max = float('-inf')
# for i in list:
#     if i != first_max and i > second_max:
#         second_max = i
# print(second_max)      

                                        # OR

# Recursion:- 
# 1.function it self calls is called Recursion.
# 2. base condition giving is very important to execute when we dont give base condition then it executes infinite times

# EX:- Factorial of a number by using Recursion

# def fact(n):
    # if n == 1 or n == 0:
    #     return 1
#     return n * fact(n-1)
# print(fact(4))


# def printer(n):
#     if n ==1 or n == 0:
#         return
#     print(n)
#     printer(n-1)
#     print(n)
# printer(10)    




# print n numbers by using n  numbers

# def print_n_num(n):
#     if n == 0:
#         return
#     print_n_num(n-1)
#     print(n)
# print_n_num(10)    


# print nth no of fibanocci series

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)  
# print(fib(10)) 


#print exponent of a number by using recursion


# def exponent(n,k):
#     if k == 0 :
#         return 1
#     return n ** exponent(n, k-1)
# print(exponent(3,2))


# sum of n numbers by using Recursion

# def sum_of_n_num(n):
#     if n ==0:
#         return 0
#     return n + sum_of_n_num(n-1)
# print(sum_of_n_num(10))



# check if string is palindrome

# str1 ='MALAYALAM'
# def check_palindrome(input_str):
#     if len(input_str) <= 1:
#         return True
#     return (input_str[0] == input_str[-1]) and check_palindrome(input_str[1:-1])
# print(check_palindrome(str1))


# sum of digits using recursion

# num1 = 54672
# def find_sum(input_num):
#     if input_num <= 0:
#         return 0
#     return(input_num % 10) + find_sum(input_num // 10)
# print(find_sum(num1))


# reverse a string using recursion

# str1 = 'desktop'
# def rev_string(input_num):
#     if len(input_num) <= 1:
#         return input_num
#     return input_num[-1] + rev_string(input_num[0:-1])
# print(rev_string(str1))
    

# find max element  in a list using recursion


# list1 = [-1,2,3,53,45,95]
# def find_max_value(input_list):
#     if len(input_list) == 0:
#         return 'No Max'
    
#     if len(input_list) == 1:
#         return input_list[0]

#     rem_max = find_max_value(input_list[1 : ])
#     # return input_list[0] if input_list[0] > rem_max else rem_max
#     #                     OR

#     if input_list[0] > rem_max:
#         return input_list[0]
#     else:
#         return rem_max
# print(find_max_value(list1))
 


# printing a list in reverse order using recursion

# list1 = [1,3,5,6,7,8]
# def rev_list(input_list):
#     if input_list <= 1:
#         return input_list
#     return len(input_list)-1 + rev_list(input_list[0 :])
# print(rev_list(list1))
    


#                                                      Dictionary Problems

# find how many times the  keys return in the list

# list =[1,2,'string',3,2,2,1,3,4]
# freq ={}
# for i in list:
#     if i not in freq:
#         freq[i] =1
#     else:
#         freq[i] += 1
# print(freq)        

# print duplicates in dictionary and unique values in dictionary by using above freq dictionary

# for i,j in freq.items():
#     if j == 1:
#         print(i,"is unique")
#     else :
#         print(i,"it have duplicates") 



# print the lenth of strings in dictionary 

# list = ['naresh','gopal','midhilesh']
# freq = {}
# for i in list:
#     freq[i] = len(i)
# print(freq)    


# Given a string, return a dictionary where keys are characters and values are their occurrence.

# str1 = 'MANMADHAN'
# freq = {}
# for i in str1.lower():
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
# print(freq)            


# Given two lists of equal length, create a dictionary where one list contains keys and the other contains values.

# list1 = ['car1','car2','car3']
# list2 = ['tesla','fortuner','xuv700']
# output = {}
# for i in range (len(list1)):
#         output [list1[i]] = list2[i]
# print(output)        


# Given a dictionary, find the key with the highest value.
# float('-inf') is nothing but finding minimum number in a list
# float('inf') is quite opposit finding maximum number in a list

# dict = {'naresh' : 10,'gopal' : 45, 'khaseem': 97}
# max_value = float('-inf')
# max_key =''
# for key,value in dict.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
# if max_value !=float('-inf'):        
#     print(max_key)  
# else:
#     print('Dictionary is Empty So No Max Key')   



# Given a list of numbers, return a dictionary of elements that appear more than once along with their counts.


# list = [1,3,4,67,7,8,7,8,3,9,3,8,9,8]
# output_dict = {}
# output_dict2 ={}
# for i in list:
#     if i not in output_dict:
#         output_dict[i] = 1
#     else:
#         output_dict[i] += 1  
# for i,j in output_dict.items():
#     if i not in output_dict2 and j>1:
#         output_dict2[i] = j
# print(output_dict2)        



#  Swap keys and values of a dictionary. Store keys in a list.

# dict = {'1' : 2, 'str' : 4,'55' : 12,'apple' : 11,'str2' : 2 }
# output_dict = {}
# for i,j in dict.items():
#     if j in output_dict:
#         output_dict[j].append(i)
#     else:    
#         output_dict[j] = [i]
# print(output_dict)        




# Given two dictionaries, merge them into one. If a key exists in both, sum their values.


# dict1 = {'k1' : 1,'k2' : 2,'k3' : 3}
# dict2 = {'k1' : 5,'k2' : 6,'k4' : 10}
# output_dict ={}
# for i,j in dict1.items():
#     output_dict[i] = j
# for i,j in dict2.items():
#     if i in output_dict:
#         output_dict[i] += j
#     else:
#         output_dict[i] = j        
# print(output_dict)     


# Find if 2 strings are anagrams

# def check_anagram(str1,str2):
#     dict1 ={}
#     for i in str1:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1


#     for j in str2:
#         if j not in dict1:
#             return False
#         else:
#             dict1[j] -= 1


#     for i,j in dict1.items():
#         if j!= 0:
#             return False
#     return True
# print(check_anagram('Ajay','jAya'))                        


#                                                  STRING PROBLEMS


# reverse a string

# str = "naresh"
# reverse_str = str[: : -1]
# print(reverse_str)

# approch2
# ---------------

# temp_str =''
# for i in str:
#     temp_str = i + temp_str
# print(temp_str)    

# Given an algebric expression , remove brackets
# inp:- "a+((b+c)+d)" output:- a+b+c+d


# str = "a+((b+c)+d)"
# new_str = ''
# for i in str:
#     if not (i == '(' or i == ')'):
#         new_str += i
# print(new_str)  


# or 


#     if i == '(' or i == ')':
#         continue
#     else:
#         new_str += i
# print(new_str)    



# or    


#     if i not in ['(',')','[',']','!']:
#         new_str += i 
# print(new_str)


# counting no of brackets and no of opening brackets and no of closing brackets in a string


# str = "a+((b+c)+d)"
# total_count = 0
# opening_bracket_count = 0
# closing_bracket_count = 0


# op_bracket = ['(','[','{']
# clo_bracet = [')',']','}']
# for i in str:
#     if i in op_bracket or i in clo_bracet:
#         total_count += 1
#     if i in op_bracket:
#         opening_bracket_count += 1
#     if i in clo_bracet:
#         closing_bracket_count += 1
# print(total_count)
# print(opening_bracket_count)
# print(closing_bracket_count)                


# compare the string is palindrome or not


# str = 'naresh'
# low = 0
# heigh = len(str) - 1
# flag = False
# while low < heigh:
#     if str[low] != str[heigh]:
#         flag = True
#         break
#     low , heigh = low + 1, heigh - 1
# if flag:
#     print('Not a Palindrome')
# else:
#     print('palindrome')        


#                         OR



# def check_is_palindrome(input_str):
#     low = 0
#     heigh = len(str) -1
#     while low < heigh:
#         if input_str[low] != input_str[heigh]:
#             return False
#         low , heigh = low + 1, heigh - 1

#         return True
# print(check_is_palindrome(str))   



# print non repeated vowels


# str = 'take you forward is awesome'

# freq ={}
# new_freq = {}
# vowels = 'aeiou'

# for i in str:
#     if i  in vowels:
#         if i not in freq:
#             freq[i] = 1
#         else:
#             freq[i] += 1
# print(freq) 

# for i,j in freq.items():
#     if j == 1:
#         new_freq[i] = j 
# print(new_freq)
   

# find the largest word in a string


# str = 'google docs are much better than word docs'
# new_list = str.split(' ')
# str_le = new_list[0]
# for i in new_list:
#     if len(i) > len(str_le):
#       str_le = i
# print(str_le)        

# find all the largest words

# str = 'google docs are much better than word docs'
# word_list = str.split(' ')
# max_string = word_list[0]
# max_ele_list = []
# for i in word_list:
#     if len(i) > len(max_string):
#         max_ele_list.clear()
#         max_ele_list.append(i)
#         max_string = i
#     elif len(i) == len(max_string):
#         max_ele_list.append(i)
        
# print(max_ele_list)        



# return the largest palidrome in a string

# str = "abccbc" #there are a b c cc bccb cbc
# output = ''
# def palindrome(str):
#     low = 0
#     heigh = len(str) -1
#     while low < heigh:
#         if str[low] != str[heigh]:
#             return False
#         low , heigh = low + 1, heigh - 1

#         return True

# palindrome_ss_list =[]
# for i in range(0,len(str)):
#     for j in range(i + 1,len(str) + 1):
#         if palindrome(str[i : j]):
#             palindrome_ss_list.append(str[i : j])
# for i in palindrome_ss_list:
#     if len(i) >  len(output):
#         output = i           
# print(output)            

     
# find weather it is sub string or not print the sub string of first index

# str = 'takeuforward'
# sub_string = []
# input = 'forward'
# flag = False
# for i in range(0,len(str)):
#     for j in range(i+1, len(str) + 1):
#        sub_string = str[i : j]
#        if sub_string == input:
#             print(i)
#             flag = True
#             break
#     if flag == True:
#         break   


# by using single for loop

# str = 'takeuforwardforward'
# input = 'forward'
# for i in range(len(str)):
#     if input == str[i : i + len(input)]:
#         print(i)
#         break
    

# 1.swapping two variables in different ways

# a,b = 10,20
# a,b = b,a 
# print(a,b)

# or


# c = a
# a = b
# b = c
# print(a,b)

# or

# a = a + b
# b = a - b
# a = a - b
# print(a,b)

# or

# num1 ^ 0 = num1
# num1 ^ num1 = 0

# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a,b)


#2. check the list is sorted or not


# code for acending order
# list1 = [1,5,3,4,5]
# flag = True
# for i in range(len(list1)-1):
#     if list1[i] > list1[i+1]:
#         flag = False
#         print("not sorted")
#         break
# if flag:
#     print('sorted')



# or

# code for decending order

# list1 = [5,4,3,2,1]
# flag = True
# for i in range(len(list1)-1):
#     if list1[i] < list1[i+1]:
#         flag = False
#         print("not sorted")
#         break
# if flag:
#     print('sorted')



#3. merge two sorted lists into a single list in the form of sorted

    




