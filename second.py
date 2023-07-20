# import calendar
# print(calendar.month(2023,4))
# import keyword
# print(keyword.kwlist)
# import functions
# functions.greet()
# functions.calulator(23.34)
# import math
# x=12.3
# print(math.ceil(x))
# x=-15
# print(math.fabs(x))
# x=5
# print(math.factorial(x))
# x=[12,22,44,54,33]
# print(math.fsum(x))
# print(math.sqrt(16))  
# import keyword
# print(keyword.kwlist)
# for i in range(10):
#     print(i)
# a="ankit"
# print(type(a))
# score=19
# # if score>=5:
# #     print("pass")
# # else:
# #     print("fail")   
# print("pass")if score>5 else print("fail")     

# class A:
#     def fun1(self):
#         print("this is inheritance A")  
# class B(A):
#     def fun2(self):
#         print("this is inheritance B")  

# object=B()
# object.fun1()
# object.fun2()

class A:
    def fun1(self):
        print("this is inheritance A")
class B(A):
    def fun2(self):
        print("this is inhetitance B")
class C(B):
    def fun3(self):
        print("this is inhertance C")        
object=C()
object.fun1()
object.fun2()  
object.fun3()           
