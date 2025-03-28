# * * * * * print this pattern
# a = 6
# for i in range(0,a):
#     for j in range(0,a):
#         print('*', end=' ')
#     print()     


# # or

# # print a right angle triangle

# a =6
# for i in range(0,a):
#     for j in range(0,a):
#         if i >= j:
#             print('*', end=' ')
#     print()    


#print upper right angle triangle  


# a =6
# for i in range(0,a):
#     for j in range(0,a):
#         if i <= j:
#             print('*', end=' ')
#         else:
#             print(' ', end= ' ')    
#     print()    


# print a pyramid shape

# a =6
# for i in range(0,a-1):
#     for j in range(0,a):
#         if i >= j:
#             print('*', end=' ')
#     print()    
# for i in range(0,a-1):
#     for j in range(0,a):
#         if i <= j:
#             print('*', end=' ')
#     print()    

# print boundary elements in a square
# a =6
# for i in range(0,a):
#     for j in range(0,a):
#         if i in [0, a-1] or j in [0,a-1] or i + j == a - 1 or i == j:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')    
#     print()     


# *         * 
# * *     * * 
# *   * *   *       this pattern code
# *   * *   *
# * *     * *
# *         *



# a =6
# for i in range(0,a):
#     for j in range(0,a):
#         if j in [0,a-1] or i + j == a - 1 or i == j:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')    
#     print()         




# * * * * * * 
#   *     *   
#     * *         this pattern code
#     * *
#   *     *
# * * * * * *



# a =6
# for i in range(0,a):
#     for j in range(0,a):
#         if i in [0, a-1] or i + j == a - 1 or i == j:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')    
#     print()     



# 1 
# 2 2 
# 3 3 3
# 4 4 4 4          this pattern
# 5 5 5 5 5


# n = 6
# for row in range(1,n):
#     for col in range(1,n+1):
#         if row >= col:
#             print(row,end = ' ')
        
#     print()        

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10                  this pattern
# 11 12 13 14 15 
# 16 17 18 19 20 21 

# num = 6
# count =1
# for i in range(num):
#     for j in range(num):
#         if i >= j:
#             print(count,end = ' ')
#             count += 1
#     print()        



#      * 
#     * * 
#    * * *
#   * * * *      this pattern
#  * * * * *


# n = 6
# for i in range(1,n):
#     for k in range(0,n-i):
#         print(' ',end = '')
#     for j in range(1,n+1):
#         if i >= j:
#             print('*',end = ' ')
        
#     print()        



#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
#  * * * * *     code for rombus
#   * * * *
#    * * *
#     * *
#      *


# n = 6
# for i in range(0,n):
#     for k in range(0,n-i):
#         print(' ',end = '')
#     for j in range(1,n+1):
#         if i >= j:
#             print('*',end = ' ') 
#     print()    
# for i in range(n - 1, 0, -1):
#     for k in range(n - i):
#         print("", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()


#       *
#      * *
#     *   *
#    *     *              this pattern code
#   *       *
#  * * * * * *


# n = 6
# for i in range(0,n):
#     for k in range(0,n-i):
#         print(' ',end = '')
#     for j in range(0,n):
#         if j == 0 or i == n-1 or i == j:
#             print('*',end = ' ')
#         else:
#             print(' ',end=' ')     
#     print()        



# print fibanocci series


# num1,num2 =0,1
# for i in range(0,5):
#     for j in range(0,5):
#         if i >= j:
#             print(num1,end = ' ')
#             # temp = num1 +num2
#             # num1 = num2
#             # num2 = temp

#             # or
#             # num1,num2 = num2,num1 + num2
#     print()        



# print alphabets in series

# count = 65
# for i in range(0,5):
#     for j in range(0,5):
#         if i >= j:
#             print(chr(count),end = ' ')
#             count += 1
#     print()        



# merge two sorted list into a new string in sorting order

# using 2 pointer method


#         1 
#       2 1 2 
#     3 2 1 2 3                this pattern
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5


# n = 5
# for i in range(n):
#     for k in range(n - i - 1):
#         print(' ',end = ' ')
#     start = i + 1  
#     rev_ord = False  
#     for j in range(2 * i + 1):
#         print(start,end = ' ')
#         if start == 1:
#             rev_ord = True
        
#         start = start - 1 if rev_ord == False else start + 1
#     print()    
   
