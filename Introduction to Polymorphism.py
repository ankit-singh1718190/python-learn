# same object having defferent behaviers
#Learn Coding
print(len("ankit"))
print(len(["ankit","singh"]))

# methods Overloading 
class A:
    def ankit(self):
        print("welcome")
    def ankit(self,fristname=''):
        print("welcome","fristname") 
    def ankit(self,fristname='',lastname=''):
        print("welcome",fristname,lastname) 
obj=A()
obj.ankit()
obj.ankit("singh")
obj.ankit("singh is king")

