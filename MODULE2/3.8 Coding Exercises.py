f = open("newfile copy.txt", "r")
print(f.read())
f.close()

f = open("newfile copy.txt", "r")
print(f.readline(12))
f.close()

f = open("newfile copy.txt", "r")
for x in f:
    print(x)
f.close()

import os
os.remove("newfile copy.txt")