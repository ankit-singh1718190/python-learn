# A function calling itself again and again 
# def ankit():
#     print("singh")
#     ankit()
# ankit()    
# import sys
# print(sys.getrecursionlimit())
# def singh():
#     print("new")
#     singh()

import sys
sys.setrecursionlimit(5000000) 
print(sys.getrecursionlimit())
def old():
    print("i am ankit singh")
    old()  
old() 
def greet ():
    global i
    i+=1
    print("hello",i)
    greet()
greet()        
# a funcation is calling itself again again 


       