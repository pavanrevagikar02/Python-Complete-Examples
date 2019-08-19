# how to import modules
def add(a,b):
    result=a+b
    print(result)
    return result

# # varialbes in modules
#
person1 = {
  "name": "nivya",
  "age": 23,
  "country": "thiland"
}
#
# # Re-naming a Module
# #You can create an alias when you import a module, by using the as keyword:
#
person1 = {
  "name": "nivya",
  "age": 23,
  "country": "thiland"
}
#
# #Built-in Modules
# #There are several built-in modules in Python, which you can import whenever you like.
import keyword
x = keyword.kwlist
print(x)

#There is a built-in function to list all the function names
# (or variable names) in a module. The dir() function:
#
# import keyword
# a=dir(keyword)
# print(a)

def add(a,b):
    return a+b
def prod(a,b):
    return a*b;
def divide(a,b):
    return a/b;