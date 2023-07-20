# def div(a,b):
#      print(a/b)
# def new_div(func): 
#      def inner(a,b):
#           if a<b:
#                a,b=b,a    
#           return func(a,b)
#      return inner      
# div1=new_div(div)
# div1(4,5)

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} called successfully")
#         return result
#     return wrapper

# @log_decorator
# def add(a, b):
#     return a + b

# result = add(2, 3)
# print(result)
# def decoder(fun):
#     def inner():
#         fun()
#         print("enhanching funcation")
#     return inner 
   
# def num():
#     print("I am Ankit Singh")
#     print("This is my laptop")
# a=decoder(num)
# a()    
# a=[]
# for i in range(100):
#     if i%3==0:
#         a.append(i)
# print(a)
# a=[i for i in range(100) if i%3==0]
# print(a)
#dic1={i:f"item {i}" for i in range(1,100) if i%3==0}
# dic1={i:f"Item {i}" for i in range(5)}
# dic2={value:key for key, value in dic1.items()}

# print(dic1,"\n",dic2)
   
a=10
print(a)