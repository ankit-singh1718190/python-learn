# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print() 
# for i in range(7,1,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print() 
# for i in range(1,7):
#     for k in range(1,7-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()    
# for i in range(1,7):
#     for k in range(1,7-i):
#         print(" ",end="")
#     for j in range(1,(2*i-1)+1):
#         print("*",end="")
#     print() 
# break Statement
# av=5
# x=int(input("How many Candies you want"))
# i=1
# while i<=x:
#     if i>av:
#         break

#     print("candy")
#     i=i+1
# print("bye") 
# av=8
# a=int(input("How many hello you want"))
# i=1
# while i<a:
#     if i>av:
#         print('out of stock')
#         break
#     print("hello")
#     i=i+1
# print('hii')

# for i in range(1,101):
#     if i%3==0 or i%2==0:
#         continue
#     print(i)

   
# for i in range(1,101):
#     if i%2!=0:
#         pass
#     else:
#         print(i)
# a= int(input("enter the number"))
# if a%2==0:
#     print("number is even")
# else:
#     print("number id odd")    
# class DemoClass:
    
#     def showvalue(self,a,b):
#         print(a+b)
       
# object=DemoClass()   
# object.showvalue(2,3)   
# class DemoClass:
#     def __init__(self):
#         print("This is a constructors")
#         print("i am ankit singh")
# object=DemoClass()  
# class A:
#     def displayA(self):
#         print("hii")
# class B(A):
#     def displayB(self):
#         print("hello")
# class C(B):
#     def displayC(slef):
#         print('ner')  
# object=C()
# object.displayA()  
# object.displayB() 
# object.displayC() 
# smae object having defferent behaviours
# print(4+5)
# print("4"+"5") 
# print(len("ankit"))  
# print(len(["ankit","singh"]))               
# class A:
#     def show(self):
#         print("hello")
#     def show(self,fistname=''):
#         print("hello",fistname)  
#     def show(self,fistname='',lastnmae=''):
#         print("hello",fistname,lastnmae)
# object=A()   
# object.show()        
# object.show("ankit")
# object.show("ankit")
# class A:
#     def show(self,fristnmae="",lastname=""):
#         print("welcome",fristnmae,lastname)
# object=A()
# object.show()
# object.show('ankit')
#overriding 
# class A:  #parent class
#     def show(self):
#         print("this is parent class method")
# class B(A): #child class
#     def show(self):
#         print("this is child class method")
# object=B()
# object.show() 
# class A:
#     def show(self):
#         print("this is parent method")
# class B(A):
#     def show(self):
#         super().show()
#         print("this is child class")
# object=B()
# object.show()   
# polymorphism
# same object having defferent behiver
# overloading methods
#whenever class more then one mtehod with same name and defferent type
#parmeter it's called overloading
# class A():
#     def show (self):
#         print("hello")
#     def show (self,fristnmae=""):
#         print("hello",fristnmae)
#     def show (self,fristname="",lastname=""):
#         print("hello",fristname,lastname)
# object=A() 
# object.show()
# object.show("ankit") 
# object.show("ankit singh")  
#overriding
# whenever we writing method name with same signature in parent and 
#child class 
# class A:  #prent class
#     def show(self):
#         print("this is parent class")
# class B(A):
#     def show(self):
#         super().show()
#         print("this is child methods")
# object=B()
# object.show() 
# class A:
#     def run(self):
#         for i in range(5):
#             print("ankit")
# class B:
#     def run(self):
#         for i in range(5):
#             print("a")  
# t1=A()
# t2=B()
# t1.run()   
# t2.run()    
# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("ankit")
#             sleep(1)
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("sing")
#             sleep(1)
# t1=A()
# t2=B()
# t1.start()
# t2.start() 
# # Python Encapsulation
# class A:
# #     _a=10#protected
# #     __b=20#private
# #     def show(self):
# #         print("a=",self._a)  
# #         print("b=",self.__b)  
# # object=A()
# # object.show()  
# # print("out side of class",object._a)  
# # import keyword
# # keyword.kwlist 
# # import keyword
# # keyword.kwlist

# a=2.3
# print(type(a))
# a=[12,3,3.4,"ankit"] #list
# print(type(a))
# a=("ankit",2.5,3) #tuple
# print(type(a))
# a={2,2.5,"ankit"}
# print(type(a))
# a={"ankit":1}
# print(type(a))
# print(a.get("ankit")) 
# a=["ankit","ankit",2.5,2.5,4]
# #extend
# b=["aha",2,4,5.6]
# a.extend(b)
# print(a)
#copy methods
# a=[1.2,3,3,1,5,6,7,8,9.0]
# #b=a.copy()
# b=a[:]  
# print(b)
#b=[12,45,43,22,1,6,78,8,9]
# x=[1,2,3]
# y=[4,5,6]
# z=zip(x,y)
# print(list(z))
# a={"ankt","ankush","aman",3.5,6,9}

# print(a)
# a=13
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# a=float(input("Enter tha frist number: "))
# b=float(input("Enter the second number: "))
# print("press 1 for addition \npress 2 for  subtraction \npress 3 for multiplication \npress 4 for division")
# c=int(input("enter your choice from 1-4: "))
# if c==1:
#     print(a+b)
# elif c==2:
#     print(a-b)
# elif c==3:
#     print(a*b)
# elif c==4:
#     print(a/b)
# else:
#     print("invalid")  
# for i in range(1,11):
#     print(i*2)
# a=float(input("enter the frist number"))
# b=float(input("enter the scond number"))
# print("press 1 for addition \npress 2 for subtraction")
# c=int(input("chose your option from 1-4: "))
# if c==1:
#     print(a+b)
   
# a=12
# b=2
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)
# logical operater
# a=12
# b=2
# print(a<b and a>b)
# print(a>b or a<b)
# print(not(a<b and a>b))
# #bit wise operation
# a= 5&6
# print(a)
# b=5|6
# print(b)
# c=5^6
# print(c)
# a=(~5)
# print(a)
# a=12
# print(a)

# # a=float(input("enter the frist number ="))
# # b=float(input("enter the second number ="))
# # print("press 1 for addition \npress 2 for subtraction")
# # c=int(input("enter the number 1- 2: "))
# # if c==1:
# #     print(a+b)
# # elif c==2:
# #     print(a-b)   

# a=2
# b=3
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)  

for i in range (1,11):
    print(2, X *1,2*i)


# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)







       





     




