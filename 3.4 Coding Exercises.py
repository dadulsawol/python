f = open("codingexercise.txt", "w")
f.write("I like that the syntax is easy to read!")

f = open("codingexercise.txt", "a")
f.write("\nI wanna become data analyst")
f.write("\nI wanna become data analyst")
f.write("\nI wanna become data analyst")

f = open("codingexercise.txt", "r")
print(f.read())
f.close()