#file is memory location
#store data peremanlty
#  read write  , create, append
# f=open ("C:\\Users\\ADMIN\\Desktop\\python\A.txt","w")
# f.write("learn data code\n Ankit | singh")

# f=open ("C:\\Users\\ADMIN\\Desktop\\python\A.txt","r")
# print(f.read(30))
try:
    f=open ("C:\\Users\\ADMIN\\Desktop\\python\A.txt","r")
    print(f.readline())
except: 
    print("file not avable")
else:
    f.close()  
    print("file closed")     


