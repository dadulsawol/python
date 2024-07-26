### diffent kinds of exeption we can encounter

# raise keyword let us define errors 
n = -5

if n < 0:
    raise Exception("No negative numbers allowed!")

# SyntaxError when code is not written correctly
# forgot the colon ":" in this example
cats = 11
if cats > 10
    print("Are you sure?")

# Assertions are boolean expression that makes sure
# that the condition return True
employee_of_the_year = "Roger"

assert employee_of_the_year == "Roger"
assert employee_of_the_year == "Suzanne"

# ZeroDivisionError occurs when you divide by zero
1/0

# TypeError occurs when an operation is performed
# on an incorrect or unsupported object type
50 ** "two" 

### How to counter exceptions

# we use try and except block to spot and handle them
# example 1
try:
    print(random_varialble)
except:
    print("Exception alert!")

# example 2
try:
    print(x + "macarons")
except NameError:
    print("Please define you variable.")
except IndentationError:
    print("Please be careful when indenting your code")
except:
    print("Something else went wrong. We need to figure it out!")

# example 3 we can use 'else'
try:
    print(500+4305)
except:
    print("This operation cannot be performed.")
else:
    print("No issues here!")

# example 4 finally block will run the code even
# if there is an error
try:
    print(h)
except:
    print("There's something wrong with our program!")
finally: 
    print("Let's run our program anyway")
    