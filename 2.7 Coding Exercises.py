#coding exercise

#1
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3,
             "milk": 2, "oranges": 4}

alreadyIncart_remove = groceries.pop("oranges")
print(groceries)

#2
speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}

names = speakers.keys()
print(names)

#3
students = {"Carl": 93, "Quentin": 60, "John Y.": 90, "Peter": 59, 
            "Max T.": 75, "Joseph": 80, "Jone": 65, "Jorge": 67,
            "Ben": 84, "Jerome": 90, "Rick": 60, "Max G.": 70,
            "John P.": 60, "Vince": 90}

search = students.get("Jorge")

if search >= 70:
    print("Passed,", + search)
else:
    print("Failed,", + search)
