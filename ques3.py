num=int(input("enter a number"))
temp=num
product=1
while num>0:
    product=product*num
    num=num-1
print("the factorial of {} is {}".format(temp,product))
    
