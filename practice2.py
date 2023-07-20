# class DemoClass:
#     a=23
#     def __init__(self):
#         print("this is constructore")
#     def showvalue(self,a,b):
#         print(a+b)    


# object=DemoClass()
# object.showvalue(20,20)

# class Demo:
#     def __init__(self):
#         print("this is constractor")
#     def New(self,a,b):
#         print(a+b)
# object=Demo()
# object.New(2,3) 
# #what is inheritance in python
# #single inheritance, and multi inheritance ,mulitpa
# # inheritance 
# class A:
#     def displayA(self):
#         print("This is inheritance A")
# class B(A):
#     def displayB(slef):
#         print("this is a inheritance B")
# class C(B):
#     def displayC(self):
#         print("this is a inhertance C")        
# object=C()
# object.displayA()
# object.displayB()
# object.displayC()

# class A:
#     def displayA(self):
#         print("This is inheritance A")
# class B:
#     def displayB(slef):
#         print("this is a inheritance B")
# class C(A,B):
#     def displayC(self):
#         print("this is a inhertance C")        
# object=C() 
# object.displayA()
# object.displayB()
# object.displayC()
# Encaplsulation in python
#getter and setter
#It means that the same function name can 
#be used for different types.
# class Ws:
#     def display(self,name=''):
#         print("Welcome to india "+name)
# object=Ws()
# object.display()  
# object.display("python") 

class Ws:
    def display(self):
        print("welcome to india") 
class IIP(Ws):
    def display(self):
        super().display()
        print("welcome to india informaton")

object=IIP() 
object.display() 

# how to print without a newline in python 
# print("hii",end="")
# print("i am ankit singh",end="")  
# print("i am working on python ") 
# what are keywords in python 
# if, else, true, false,lambada, and ,return, global
# for,while,elif ,as ,or,pass, import,
#numeric: int,flot,complex
# list tuple range set dict, bool
# what is defference between python arrays and me
# d={
#     'name':'python',
#     'fees':8000,'duration':'2Month'

# }  
# for i in d:
#     print(d[i])
# f=d['fees'] 
# n=d['name']  
# print(f) 
# print(n) 
#slicing
# a="welcome to india"
# # print(a[0:12])
# # print(a[-1])
# print(a[0:])
# print(a[0:7])
# print(a[0::2])
# print(a[-1::-2])
# print(a[-1::-1])
# def my__funcation():
#     print("i am ankit singh")
# my__funcation() 
# fibonnaci series
# a=int(input("enter the number"))
# x=0
# y=1
# z=0
# while(z<=a):
#     print(z)   
#     x=y
#     y=z
#     z=x+y
a=[1,3,23,23,15,64,3,43,53,2,3,4,34,5,78,9]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)  
#vcg sbdfshgfhfhgfbgf     re h  vfbs      r tr

a="shivani Ankit "
for i in range(200):
    print(a)

    