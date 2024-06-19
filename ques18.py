string=input("enter a string")
str2=input("enter another substring")
if(len(str2) != len(string)):
    print("its not an anagram")
else:
    i=0
    while i<len(string):
        if(string[i] in str2):
            i=i+1
        else:
            break
    if i==len(string):
        print("its an anagram")
    else:
        print("its not an anagram")
