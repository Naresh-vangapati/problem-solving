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

    




