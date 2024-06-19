scale=input("enter scale")
if scale=='c' or scale=='C':
    temp=int(input("enter temperature in degree celsius"))
    farenheit=1.8*temp + 32
    print(farenheit)
else:
    temp=int(input("enter temperature in degree farenheit"))
    celsius=float ((5*(temp-32))/9)
    print(celsius)
