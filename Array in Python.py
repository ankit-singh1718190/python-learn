#arry can store only one type of data
#containers which are able to store more than one item at the same time. Specifically, they are an ordered collection of elements with every value being of the same data type.
import array as arr
#from array import*
vals = arr.array('i',[12,32,45,65,76,78,89])
print(vals)

import array as arr
a=arr.array("i",[12,32,32,32,32,445,54,-5])
print(a)

from array import*
b=array("I",[12,23,44,54,34,43])
# b.reverse()
# for i in range (5):
for i in range(len(b)):
    print(b[i])
# print(b.buffer_info())
# print(b.typecode)
from array import *
c=array("i",[12,34,5,66,])
newArr=array(c,typecodes,(a for a in c))
for e in newArr:
    print(e)
