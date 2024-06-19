string=input("enter a string")
suffix=input("enter the suffix")
prefix=input("enter the prefix")
if string.endswith(suffix)==True:
    print("the string has the suffix")
else:
    print("the string does not have the suffix")
if string.startswith(prefix)==True:
    print("the string has the prefix")
else:
    print("the string does not have the prefix")
