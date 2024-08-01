# r is use for reading file 
f = open("newfile.txt", "r")
print(f.read())
f.close()

# since it is a default value
# we dont need to specify them
f = open("newfile.txt")
f.close()
print("\n")

# if u want to read a specific character
f = open("newfile.txt", "r")
print(f.read(15))
f.close()
print("\n")

# read line method will return a single line
f = open("newfile.txt", "r")
print(f.readline())
f.close()

print("\n")

# we can also use loops
# allows us the whole file one line at a time
f = open("newfile.txt", "r")
for x in f:
    print(x)
f.close()

# deleting a file we need to check if the file exists
# by setting up a conditional statement
import os

if os.path.exists("newfile.txt"):
    os.remove("newfile copy.txt")
else:
    print("The file does not exitst")

# if you are already sure that the file does exists 
import os
os.remove("newfile copy.txt")