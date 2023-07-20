# # age =int(input("Enter the age"))
# # if age>=18:
# #     print("You are able for voting")
# # else:
# #     print("You are not able for voting")  
# #check  if a number is positive or negative
# num=int(input("enter the number"))
# if num>=0:
#     print("the number is postive")      
# else:
#     print("number is negative")    
# #Check if a number is even or odd
# num =int(input("enter the number"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd") 
#Check if a string is empty or not  
# *
# **
# ***
# ****
# *****
# a=int(input("enter a value 1 to 12:"))
# if a==1:
#     print("jan")
# elif a==2:
#     print("feb")
# elif a==12:
#     print("dec")
# else:
#     print("wrong input") 
# for i in range(0,5):
#   for j in range(-1,i):
#      print("*",end="")
#   print()           
# a=[12,3,43,3,23,22,32,22,33,21,212,212,222,111,232] 
# for i in a:
#     print(i)
# a="ANKIT"
# for i in a:
#     print(i)
# for i in range(11,21,2):
#     print(i)
# for i in range(1):
#     print("*",end="")
# print()    
# for i in range(2):
#     print("*",end="")
# print()
# for i in range(3):
#     print("*",end="")
# print()    
# for i in range(4):
#     print("*",end="")
# print()
# for i in range(5):
#     print("*",end="")
# for j in range(4):
#     for i in range(4-j):
#         print("*",end="")
#     print()
# for j in range(4):
#     for i in range(j+1):
#         print("*",end="")
#     print()  
# for loop and while loop for loop is definite loop and 
#while loop is indefinite loop  
# for i in range(5):
#     for j in range(i+1):
#         print("Ankit ",end="")
#     print()  
# i=1
# while i<=10:
#     print("ankit ",end="")
#     i=i+1 a
# for i in range(2,30,4):
#     print(i)
# for i in range(1,11):
#     print(2*i)
# for i in range(1,11) :
#     print("3*",i,"=",3*i)    
# i=1
# while i<=10:
#     print(i,"=",2*i)
#     i=i+1
# i=1
# while i<=10:
#     print("2*",i,"=",2*i)
#     i=i+1
#Procedural orented Programming
#oops 
# class  methods object
# class LearnOops:
#     a=10
#     def sumvalue(self):
#         print(30+20)
# demoobject=LearnOops()
# #print(demoobject.a)
# demoobject.sumvalue();   
class DemoClass:
    a=20
    def __init__(self):
        print("this is constructors")
    def showvalue(self):
        self.c=self.a*self.a 
        print(self.c)
    def showvalue1(self,a,b):
        print(a+b)   
    def showvalue2(self):
        print("this is the second funaction")     


object=DemoClass()
object.showvalue()
object.showvalue1(20,20)
object.showvalue2()
#Constructors is work automatic
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("my name is ankit ")

object = Person("ankit",25)
Person.introduce()


             