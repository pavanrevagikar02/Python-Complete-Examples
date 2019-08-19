# declaring multiple exception
# try:
#     a=5
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print('Division by zero not allowed')
# except TypeError:
#     print('Unsupported operation')
# print ('Out of try except blocks')

try:
    a=5
    b=0
    c='7'
    print(a/b)
    print(a+c)
    print(a/c),IndentationError
except(ZeroDivisionError,TypeError):
    print('Division by zero not allowed')
print ('Out of try except blocks')


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")