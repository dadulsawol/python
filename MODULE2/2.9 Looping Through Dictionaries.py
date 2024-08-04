# .items allows us to access both the key and the values for looping
# through the dictionaries
employee_1 = {"Name": "Frank", "Position": "Sales Representatives", "Email Address": "frank@company.com"}

for key, value in employee_1.items():
    print(key)
    print(value)

print("\n")

# use .key method allows us to access the KEY for looping 
characters_weapon = {"Harry Potter": "wand", "Percy Jackson": "Riptide",
                     "Katniss Everdeen": "bow and arrow", "Bilbo Baggins": "Ring"}

for name in characters_weapon.keys():
    print(name)

print("\n")

# using continue for .key method
for name in characters_weapon.keys():
    if name == "Percy Jackson":
        continue
    else:
        print(name)

print("\n")

# .values method only the values will be printed in the console
most_delicious = {"Mcdonald's": ["fried chicken", "sundae"], "Jollibee": ["fried chicken", "spaghetti"],
                  "KFC": ["gravy", "mashed potato"], "Pizza Hut": ["pizza", "pasta"]}

for items in most_delicious.values():
    print(items)

print("\n")

# using nested keyword in dictionary
# meaning there is a dictionary within the dictionary
cat = {1: {"name": "Sweetie", "age": "12", "color": "white"},
        2: {"name": "Ethel", "age": "3", "color": "orange"}}
print(cat)

print("\n")

# by using [] we can access the elements of each dictionary
print(cat[1]["age"])
print(cat[2]["name"])
print(cat[2]["color"])

print("\n")

# using {} we can create a new dictionary
# first example
cat[3] = {}
cat[3]["name"] = "Tuna"
cat[3]["age"] = "1"
cat[3]["color"] = "black"
print(cat[1])
print(cat[2])
print(cat[3])
# second example
cat[4] = {"name": "Bubbles", "age": "7", "color": "white"}
print(cat[4])
print("\n")

