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