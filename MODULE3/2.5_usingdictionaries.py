exam_scores = {"Jonathan": 85, "Erica ": 99, "Rose": 83, "Henry": 92, "Missy": 77,
               "Ashleigh": 88, "Paul": 68, "Gordon": 86, "Lisa": 98, "Kelly": 77,
               "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

# Search in dictionary
print(exam_scores["Paul"])

# Checking if data exist
check_key = "Andreww"

if check_key in exam_scores:
    print(check_key, "Took the exam") 
else:
    print("Andreww did not took the exam.")

# .get() method to return the data, if null it will return none
print(exam_scores.get("Lisa"))
print(exam_scores.get("Missy"))
print(exam_scores.get("Queenie"))

# .pop() method deleting data
# .keys() get the keys without their value
neighbors = {"Ms. Santor": "fruitcake", "Mr. Reyes": "cookies", 
             "Mrs. Dela Cruz": "cupcakes", "Mr. Tiu": "gingerbread man"}

done = neighbors.pop("Mr. Reyes")
y = neighbors.keys()

print(y) 

# .values() get all the value without their keys

w = neighbors.values()
print(w)

# .items() shows both the keys and the value

z = neighbors.items()
print(z)