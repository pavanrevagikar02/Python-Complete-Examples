# def square(x):
#     y = x ** 2
#     return y
# result = square(3)
# print(result)

# def sq(x):
#     return (x**2)
# print(sq(3))

# def add(x, y, z):
#     a = x + y
#     b = x + z
#     c = y + z
#     return a, b, c
#
# m = add(10,20,30)
# print(m)

#
# def cal(a,b):
#     sum=(a+b)
#     diff=(a-b)
#     mul=(a*b)
#     return sum,diff,mul
# t=cal(100,50)
# for i in t:
#     print(i)
#
def test():
    for x in range(10):
        print(x)
        if x == 5:
            # Stop function at x == 5
            return
test()
#
def func(name):
    message = "Hi "+name;
    return message;
name = input("Enter the name?")
print(func(name))
#
#
# def cal(a,b):
#     sum=(a+b)
#     diff=(a-b)
#     mul=(a*b)
#     return sum,diff,mul
# x,y,z=cal(10,6)
# print(x)
# print(y)
# print(z)

# def myfile(x):
#     print(2*x)
#     return
# myfile(2)
#
# def myfile(x):
#     return(2*x)
# print(myfile(2))

# def hello():
#     for i in range(10):
#         print(i)
# hello()

# def test():
#     for x in range(6):
#         # print(x)
#         if x == 5:
#             # Stop function at x == 5
#             continue
#         print(x)
# test()