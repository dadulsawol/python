import module as module

# you can change the name of file using 'as'
import module1 as m1

# another way of importing a module is using 'from'
from module2 import * 

# if you only need a specific function u can use this
from module2 import get_diff

# module 
module.greeting("April")

# module 1
a = m1.user_1
print("Hey there, " + a.name + "! Ready to do some math?")

c = m1.user_3
print("Hey there, " + c.name + "! Ready to do some math?")

# module 2
sum = get_sum(23, 34)
print(sum)

qoutient = get_quo(32, 2)
print(qoutient)

difference = get_diff(89, 9)
print(difference)