# default arguments
def d(a=23,b=40): 
    c=(a+b)
    print(c)
d()
d(12,3) 
def ankit(x,y):
    a=(x*y)  
    print(a) 
ankit(12,1)
#keywold Arguments
def sing(x=10,y=20): 
    a=(x+y)
    print(a)
sing(x=20,y=10)
sing(y=20,x=20)
#pointer Argument
def fun(*x):
    for i in x:
        print(i)
fun(12,23,32,32,32,12,3)   
fun(23,34,34,45)
fun("anit","singh") 
#Position
# keyword
# defult
# variable length
def ankit(name,age):
    print(name)  
    print(age) 
ankit("navie","29")  
def singh(x,*y) :
    for i in y:
      print(i)
singh(2,34,44,333,3,4,33,3,2,3,3,33)    
