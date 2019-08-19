# import first
# first.add(10,20)

# we are importing 1st modules of the variables

import first
a=first.data['country']
print(a)

# Renaming a module
import first as test
x=test.list[3]
print(x)

# import from module

# from modulespackages.first import add,prod
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# print("Sum = ",add (a,b))
# print("prod = ",prod(a,b))
# print("divide = ",divide(a,b)) #NameError: name 'divide' is not defined (throws error)

#The following example imports only one function - add().
from modulespackages.first import add
print("add:", add(10,20))
# calling prod() or divide() will throw an error


# You can also import all of its functions using the from...import * syntax.
from modulespackages.first import *
print("Sum of a and b :", add(1,2))
print("Product of a and b :", prod(10,7))
print("Difference of a and b :", diff(39,88))
print("Divide of a and b:", divide(100,80))