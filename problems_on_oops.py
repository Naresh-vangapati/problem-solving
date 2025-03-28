# OOPS
# __________


# why oops ? disadvantages of procedural programming languageb ?

#maintainability is tough which means we write the code different places then it is hard to 
# integrate them then we use oops by using object and classes

# class :- class is nothing but blue print of object
# object :- object is instance of class
# when we create one class then we can create multiple objects
#we can start write a class by using class name


# syntax:-
# _______________

# class HumanBeing:
#     #variables
#     #methods nothing but functions
#     #another way of defining variables
# ___________________________________________


#     def __init__(self,name1,age1,dob1):
#         self.name = name1
#         self.age = age1
#         self.dob = dob1
#         print("I am a human constructor")

#     def self_intro(self):
#         print("Hi ,I am",self.name)

#     def greet(self):
#         print("Hello My Name Is Naresh")    


# #objects
# ______________

# human1 = HumanBeing('suresh', '34', '2feb')
# human2 = HumanBeing('naresh', '34', '2feb')
# human3 = HumanBeing('ramesh', '34', '2feb')
# human4 = HumanBeing('gireesh', '34', '2feb')


# #variables
# #one way of adding variables
#____________________________________

# human1.name = "naresh"
# human1.dob = "2nd feb"
# human2.name = "gopal"


# print(human1.name,human1.dob)
# print(human2.name)

# print(human1)
# print(type(human1))

# #method invoking
# ___________________

# human2.self_intro()
# human3.self_intro()
# human2.greet()


#constructor
#_____________

# constructor is actually a function it calls automatically when you declared object

# syn for constructor:-

# init stands for intialize

# def __init__(self):
#     print("I am a human constructor")


# self keyword:- 
#________________

# self is nothing but this keyword in javascript

# it is used to indicate current object in our program

# we dont need to pass arguments to self it is automatically added by compiler


#Types of Variables:-
# _________________________

# variables are two types

# 1. Instance variables
# __________________________

# where it is specific to the instance or objects for ex :- name ,dob
#when you change the value of the object then all the class values are chenges in this variables
# we cant access instance variables by using class name like HumanBeing

# 2. Class Or Static variables
# ___________________________________

# variable which is belongs to class it is called class or static variable.
#  whose value is same to all the objects or instances in the class
# by using class name we can access class variables or static variables




# Types of Methods
# _____________________

# 1.Instance methods
# ____________________________

# any method which is using  one instance variable it is called instance methode
# we can access these methods by using object name without using class name

# 2.Static methods
# _____________________

# in static method we dont use any variables
# we can access these methods by using both instance and class name

# 3.class methods
# ____________________

# any method which works with static variables or class variable is called class method
# we can access these methods by using both instance and class name


# class polygone():
#     total_count = 0
#     def __init__(self,n_side1):
#         polygone.total_count += 1           # constructor function it is also instance method because we are using  a instance variable called n_side1
#         self.n_side1 = n_side1
#         print("polygone is created")
    
#     def calculate_area(self):                                   #instance method because we are using hear also n_side1 named instance variable
#         print("Area of polynomial is", self.n_side1 ** 2)

    
#     @classmethod 
#     def reset_total_count(cls):                        #class method because we are using a class variable which is total_count = 0
#         cls.total_count = 0
#         print("Total count is now zero")   


#     @staticmethod
#     def info():                                            #static method  because here we dont use any variable 
#         print("This is a polygone which has n sides depending on input .. has total 3 methods")    


# poly1 = polygone(3)
# poly2 = polygone(4)
# print(polygone.total_count)
# polygone.reset_total_count()
# print(polygone.reset_total_count)
# polygone.info()


# 4 main concepts of oops

# 1.Inheritance
# ___________________

# child class(sub class or derived class) inheriting properties from parent class(or super class or base class).

# class User:
#     #username,adress,dob,gender
#     def __init__(self,name,dob,gender):
#         self.name = name
#         self.dob = dob
#         self.gender = gender
#         print("User object created with name,dob,and gender")
        
#     def change_address(self):
#         print("Address changed")

# class Teacher(User):
#     def __init__(self,name,dob,gender):
#        super().__init__(name,dob,gender)
#        print("Teacher object Created")

#     def teach(self):
#         print("I am a Teacher and I am Teaching")


# tch1 = Teacher('naresh','28 aug','male')
# tch1.change_address()


# Types of Inheritance
# ________________________

# Single inheritance
# multiple inheritance
# ____________________________

# it inherits the properties from multiple parents for example C inherits properties from A and B at a time
# it follows method resolution order

# class Lion():
#     def roar(self):
#         print("Lion is Roaring")

# class Tiger():
#     def hunt(self):
#         print("Tiger is Hunting")

#     def roar(self):
#         print("Tiger is Roaring")    


# class Liger(Lion,Tiger):
#     def hunt(self):
#         print("Liger is Hunting")


# lg1 = Liger()
# lg1.hunt()
# lg1.roar()

# print(Liger.mro())

# multi level inheritance
# _____________________________
# it is a hiararchi of inheriting properties from the parent class B inherit properties from A and C inherits properties from the B

# class user:
#     def show_info(self):
#         print("This method give information about User")

#     def teach(self):
#         print("User is trying Teaching")    


# class Teacher(user):
#     def teach(self):
#         print("Teacher is Teaching")


# class Admin(Teacher):
#     def teach(self):
#         print("Admin is Teaching")


# adm1 = Admin()
# adm1.show_info()
# adm1.teach()

    
# 2.Abstraction
# __________________

# Abstraction is nothing but hiding the implementation or process of the data
# abstract classes has no logic it contains only the  structure of the method
# Abstract methods has no definition in that classes 
# we have to import  from abc import ABC , abstract method
# we canot create object for abstract class

# Abstract class
# __________________

# syntax for abstract class
# ________________________________

# from abc import ABC, abstractmethod

# class ATM(ABC):
#     @abstractmethod
#     def withdrawl(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass

# class SBI_ATM(ATM):

#     def withdrawl(self):
#         # SBI logic for withdrawl
#         print("SBI processing withdrawl ... come after lunch break")

#     def deposit(self):
#         # SBI logic for Deposit
#         print("Depositing Right away")  

# sbi1 = SBI_ATM()
# sbi1.deposit()



# 3.Polymorphysm
# __________________

# operator overloading
# _________________________

# it acts different with different operands
# ex:- print(2 + 3)
# print('2' + '3')

# class Polygone:

#     def __init__(self,n_side):
#         self.n_side = n_side


#     def __add__(self,other):
#         return self.n_side + other.n_side
    
#     def __mul__(self,other):
#         return self.n_side * other.n_side
    

# plg1 = Polygone(5)
# plg2 = Polygone(7)


# print(plg1 + plg2)
# print(plg1 * plg2)

    
# method overloading
# _______________________

# In python there is no method overloading and it is not supported in python but it works in other programming languages
# a function defining with same name and same functionality with different parameters is called method overloading
# indirectly can be achived with orbitary and keyword orbitary arguments

# method overriding
# ________________________

# redefining a function in a sub class which is in parent class is called method overriding

# 4.Encapsulation
# ______________________

# encapsulation is used to hide Data
# we can hide the data by using getters and setters

# class HumanBeing:
#     def __init__(self,name,ph_num,dob):
#         self.name = name
#         self.ph_num = ph_num
#         self.dob = dob
#         print("Human object is created")
       
#     def get_ph_num(self):
#         return self.ph_num

#     def set_ph_num(self,new_ph_num):
#         self.ph_num = new_ph_num
#         print("Phone number is Updated")



# hm1 = HumanBeing('sj','99999','4feb')

# hm1.get_ph_num()
# print(hm1.name)




# access specifiers => public,private,protected

# public:- that variable accessable anywhere
# private:-we can access in the class only
# we use double underscore to privatise the data

# class HumanBeing:
#     def __init__(self,name,ph_num,dob):
#         self.name = name
#         self.__ph_num = ph_num
#         self.dob = dob
#         print("Human object is created")
       
#     def get_ph_num(self):
#         return self.__ph_num

#     def set_ph_num(self,new_ph_num):
#         self.__ph_num = new_ph_num
#         print("Phone number is Updated")


# hm1 = HumanBeing('sj','99999','4feb')

# hm1.get_ph_num()
# print(hm1.ph_num)




# protected:- we can access the variables in that class or childs of that class only
# we use single underscore to protect the data


# class HumanBeing:
#     def __init__(self,name,ph_num,dob):
#         self.name = name
#         self.ph_num = ph_num
#         self._dob = dob
#         print("Human object is created")
       
#     def get_ph_num(self):
#         return self.ph_num

#     def set_ph_num(self,new_ph_num):
#         self.ph_num = new_ph_num
#         print("Phone number is Updated")



# hm1 = HumanBeing('sj','99999','4feb')
# hm1.set_ph_num('98765')
# print(hm1.get_ph_num())
# print(hm1.get_ph_num())
# print(hm1.name)
# print(hm1._dob)




