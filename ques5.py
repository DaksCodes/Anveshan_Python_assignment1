string=input("Please enter a string:")
file_name="output.txt"
with open(file_name,"w") as file:
    file.write(string)
print(f"The input has been written to{file_name}")
