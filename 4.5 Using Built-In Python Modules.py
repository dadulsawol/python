# to view all a comprehensive list of all the built-in modules in python
help("modules")

# to view all the attributes of all the modules you want to import
# type the modules name inside, for example
help("random")
print(dir("random"))

# this modules provides pseudo random numbers
from random import randint
print(int(randint(1, 1000)))

# date and time module allows us to work with data and time
import datetime

# returns the current date
t = datetime.datetime.now()
print(t)

# strftime() method makes string with the imported date and time
t = datetime.datetime(2021, 5, 17)
print(t.strftime("%B"))
print(t.year)