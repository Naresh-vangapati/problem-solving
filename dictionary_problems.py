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
