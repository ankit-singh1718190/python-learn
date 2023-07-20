#merging Two dictionaries
d1={"apple":3,"banana":1}
d2={"orange":2,"pear":4}
merged_dict={**d1,**d2}
print(merged_dict)
d3={"Graps":3,"jackfruit":5,"lime":5,"kiwi":4,
    "fig":4,"dates":5}
d4={"java apple":4,"ugni":8,"Rose Hips":7}
merged_dict={**d3,**d4}
print(merged_dict)
string=" hello    ankit  "
new_string="".join(string.split())
print(new_string)
a="madam"
b=a[-1::-1]
if a==b:
    print("palindrome")
else:
    print("not")   

a="madam"
if a==a[::-1]:
    print("string is a palindrome") 
#removing duplicate from a list
a=[1,22,2,1,2,3,3,3,4,5,4,6,5,6]
a=list(set(a))
print(a)  
a=[]
if not a:
    print("list is empty")  
a="hello world"
b=list("string")
print(b)
