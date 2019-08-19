from functools import reduce

number = [10, 20, 30, 15, 25, 35, 45]
print(number)

add= reduce((lambda x, y: x + y), number)
print(add)

sub = reduce((lambda x, y: x - y), number)
print(sub)

mul = reduce((lambda x, y: x * y), number)
print(mul)

import functools

def mult(x,y):
    return x*y
data=functools.reduce(mult, range(1, 7))
print(data)

import functools
def add(x,y):
    return x+y
data=reduce(add, range(1, 7))
print(data)

number = [10, 20, 30, 15, 25, 35, 45]
print(number)
a=reduce(lambda x,y:x+y,number)
print(a)
