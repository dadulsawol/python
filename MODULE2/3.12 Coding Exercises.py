x = 500

if x > 100:
    raise Exception("X should not be bigger than 100!")

try:
    print(variable_1)
except:
    print("Define your variable")

for i in range(6):
    print("I'm so happy!")

try:
    print(12*6)
except:
    print("The opeartion cannot be performed!")
else:
    print("The opeation can be performed!")

best_burger = "Burger King"
number_2_burger = "Mcdonalds"

assert best_burger == "Burger King"
assert best_burger == "Mcdonalds"