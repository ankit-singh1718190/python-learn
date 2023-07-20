# prime number it is divided by 1 or self
a=20
for i in range(2,a):
    if a%i==0:
        print("not prime number")
        break
else:
    print("prime")  
# i is countable variable      