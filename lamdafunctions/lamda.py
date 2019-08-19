def square(n):
    print(n*n)
square(4)

# a=lambda n:n*n
# print(a(6))
#
#
def test():
  return lambda a,b : a * b
h=test()
print(h(2,5))
#
#
# def test(a,b):
#   x= lambda a,b : a * b
#   print(x(a,b))
# test(10,20)


# def sqr(n):
#   a=lambda n:n*n
#   print(a(n))
# sqr(10)

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))
#
# a = lambda n : n * n
# print(a(4))
#
# def test(n):
#   return lambda a : a * n
# h=test(2)
# print(h(9))
#
# def test(n):
#     return lambda a : a * n
# x = test(2)
# y = test(7)
# print(x(11))
# print(y(9))
#
# n = int(input("Enter the number?"))
# def table(n):
#     return lambda a:a*n; # a will contain the iteration variable i and a multiple of n is returned at each function call
# b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i
# for i in range(1,11):
#     print(n,"X",i,"=",b(i)); #the lambda function b is called with the iteration variable i,
#
# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(num, 'x', i, '=', num * i)
#
# s=lambda n:n*n
# for i in range(1,11):
#     # print('The Square of {} is: {}'.format(i,s(i)))
#     print(s(i))
#
n = int(input("Enter the number?"))
def test(n):
    return lambda a:a*n;
b = test(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i));


def test():
    h=lambda a,b:a**b
    print(h(7,8))
test()




































































































































