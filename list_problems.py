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
