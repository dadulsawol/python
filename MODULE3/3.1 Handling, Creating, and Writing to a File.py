# opening and creating a file
f = open("newfile.txt", "x")

# opening and write
# using w, wil also overwrite any existing content
f = open("newfile.txt", "w")
f.write("Python is easy!")

# opening and reading the file
# make sure to close the file
f = open("newfile.txt", "r")
print(f.read())
f.close()

# appending or add to data into existing file
f = open("newfile.txt", "a")
f.write("\nPython is rockstar")

f = open("newfile.txt", "r")
print(f.read())
f.close()

