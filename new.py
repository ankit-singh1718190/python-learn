a=23
print(a)
a=8/2
print(a)
# // integer Division 
a=7//2
print(a)
#** power off
a=4**10
print(a)
# remainder %
a=23%3
print(a)
a=('ankit\'s "Singh"')
print(a)
a=("ankit's Singh")
print(a)
a=10*"ankitsingh"
print(a)
# fetch-------------------
a="ankit singh"
print(a[3])
print(a[-1])
print(a[:8])
print(a[0])
print(a[1])
#list in python
a=[12,22,23,45,56,67,23,45,34,55,57,67,89,78,45,23,24,]
print(a)
print(a[4])
print(a[2:])
print(a[2:5])
print(a[0:9])
print(a[-1])
print(a[-9])
# list of string
# list is mutable nature
#a=['ankit','navin','jon','mhian','singh']
#[]
#print(a[1])
a.append(12)
print(a)
(a.clear)
print(a)
a.insert(2,77)
print(a)
a.insert(4,88)
print(a)
a.remove(88)
print(a)
a.remove(77)
print(a)
a.remove(12)
print(a)
a.remove(12)
print(a)
a.remove(22)
print(a)
a.remove(23)
print(a)
a.remove(45)
print(a)
a.pop(1)
print(a)
a.pop(3)
print(a)
a.pop(7)
print(a)
a.pop(5)
print(a)
a.pop()
print(a)
del a[2:]
print(a)
a.insert(1,24)
print(a)
a.insert(3,76)
print(a)
del a[1:]
print(a)
a.extend([23,34,45,55,54,32,23,23])
print(a)
a.remove(23)
print(a)
a.remove(56)
print(a)
#Tuple in python
#tuple is tuple is immutable
#()
tup=(23,34,45,55,33,44,54)
print(tup)
#tuple is faster more then list
#set set is collection of unique elements
#{} for set
# set is not follow sequence
# it will not support duplicate values 
s={23,33,22,13,342,43}
print(s)
s={23,23,45,543,212,323}
print(s)
# dictionary
#Dictionary. Dictionaries are used to store
#data values in key:value pairs
a={1:'ankit',2:'singh',3:'navin'}
print(a)
print(a[3])
print(a[2])
a=['ankit','navin','shivi']
b=['song','dance','gym']
d=dict(zip(a,b))
print(d)
d['monika'] ='cs'
print(d)
del d['ankit']
print(d)
a='ankit'
print(id(a))
a=4
print(id(a))
a=10
b=a
print(a)
print(b)
print(id(a))
print(id(b))
a=3.5
b=int(a)
print(b)
print(type(b))
#data types in python
# none, numeric, list, tuple, set, string,range,dictionary
#numeric=int, flot, complex, bool
# complex a+bi(8+9j)
a=23
b=24
a=23+6j
print(a)
a=5
b=6
c=complex(a,b)
print(c)
#bool true and false in bool data type
a=46
b=34
c=a>b
print(c)
c=a<b
print(c)
c=a==b
print(c)
print(type(c))
a=int(True)
print(a)
a=int(False)
print(a)
a=[12,23,33,34,4]
print(type(a))
a=(23,34,44,553,32,321,13,1,)
print(type(a))
a={22,23,32,23,23,33}
print(type(a))
a={1:'ankit',2:'singh'}
print(a)
print(a[1])
print(type(a))
a=10
print(range(a))
print(list(range(10)))
a=50
print(list(range(4,50,4)))
a=4000
print(list(range(100,400,100)))
print(type(a))
a={'ankit':'iphone','navin':'onepluse','singh':'mi'}
print(a)
print(type(a))
print(a.keys())
a={'shyam':'onepluse','mohan':'iphone','anju':'redme'}
print(a)
print(a.keys())
print(a.values())
print(a.keys())
print(a.values())
print(a['shyam'])
print(a.get('mohan'))
#operators in python
x=2
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
#assignment operators in python
x=x+2
print(x)
x+=4
print(x)
x*=2
print(x)
x/=2
print(x)
a,b=4,5
print(a)
print(b)
a,b,c,d,f,g=2,3,4,5,6,8
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
#unary operators
#it work on single operand
n=2
print(n)
print(-n)
n=-n
print(n)
#relational operatores
a=40
b=50
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)
print(b!=a)
#logical operatores
# and or not two conditions
a=10
b=20
print(a<12 and b<30)
print(a<9 and b<10)
#truth table for and x, 0 0=0= y, 0 0=0
print(a<12 or b<10)
x=not x
print(x) 
#number system
#binary
#  octal and hexadecimal
#decimal (0,9) and binary (0,1)
# 8 octal(0,7)
# 16 hexadecimal (0,5)(a,f)
a=25
print(bin(25))
a=459
print(bin(a))
a=1010101
print(0b0101)
print(0b10110110)
a=282873
print(bin(a))
a=(0b101110)
print(a)
a=0b10100100100100010100100010100110
print(a)
a=25
print(oct(25))
a=234
print(hex(25))
a=0xf
print(a)
a=0xe
print(a)
#BitWise Operators
#15 video
#Complement(~)
#and(&)
#or(|)
#xor(^)
#left shift(<<)
#right Shift(>>)
a=~12
print(a)
a=~50
print(a)
a=12&13
print(a)
a=12|13
print(a)
a=12^13
print(a)
a=10<<2
print(a)
a=10>>2
print(a)
a=10<<3
print(a)
a=10>>2
print(a)
#16















