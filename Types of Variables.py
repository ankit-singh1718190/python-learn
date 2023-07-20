# Types of Variables
class A:
    def ankitA(self):
        print("welcome to india 1st state")
class B:
    def ankitB(self):
        print("welcome to india 2nd state")
     
class C():
    def ankitC(self):
        print("welcome to india 3rd state") 
class D(A,B,C):
    def ankitD(self):
        print("welcome to india 4th state")


obj=D() 
obj.ankitA() 
obj.ankitB() 
obj.ankitC()
obj.ankitD()        

