# month=int(input("Enter the month number"))
# if month==2:
#     print("28 or 29 days")
# elif month==4 or month==6 or month==9 or month==11:
#     print("30 days")  
# elif month>12 or month<1:
#     print("invalid month number")
# else:
#     print("31 days")   
month=int(input("Enter the month number")) 
l1=[4,6,9,11]
l2=[1,3,5,7,8,10,12]     
if month==2:
    print("28, or 29 days")
elif month in l1:
    print("30 days")         
elif month in l2:
    print("31 days")
else:
    print("invalid month number")    