# #Without using any function
# data=[1, 2, 3, 4, 5, 6]
# square=[]
# for i in data:
#     square.append(i**2)
# print(square)
#
#
# # using normal  (map object as output)
# data=[1, 2, 3, 4, 5, 6]
# def square(n):
#     return n*n
# list1=map(square, data)
# print(list1)            # <map object at 0x7f8304765b70>

# Converting map object to a list
# data=[1, 2, 3, 4, 5, 6,9]
# def square(n):
#     return n*n
# list1=list(map(square, data))
# print(list1)

# # with Lambda function
#
# data=[1, 2, 3, 4, 5, 6,9]
# # def square(n):
# #     return n*n
# list1=list(map(lambda n:n*n, data))
# print(list1)
#
# # Applying map to multiple sequence
#
# h1=[1, 2, 3, 4, 5,6]
# h2=[5,10,15,20,25,30]
# list1=list(map(lambda x,y:x*y,h1,h2))
# print(list1)
#
# # Appliyng map for 3 sequences
# h1=[1, 2, 3, 4, 5]
# h2=[5,10,15,20,25]
# h3=[4,6,7,8,2]
# list1=list(map(lambda x,y,z:x*y+z,h1,h2,h3))
# print(list1)

# # While we still use lamda as a aFunction, we can have a list of functions as aSequence:
# # def square(x):
# #     return (x ** 2)
# # def cube(x):
# #     return (x ** 3)
# # funcs = [square, cube]
# # for r in range(0,5):
# #     value = list(map(lambda x: x(r), funcs))
# #     print(value)
# #
square=[]
for i in range(10):
    square.append(i*i)
print(square)

# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# data=[square,cube]
# for i in range(1,10):
#     value=list(map(lambda x:x(i),data))
#     print(value)