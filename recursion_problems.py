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
    