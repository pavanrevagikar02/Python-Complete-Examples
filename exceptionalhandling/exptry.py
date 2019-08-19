# try:
#     a=5
#     b='0'
#     print(a/b)
# except:
#     print('Some error occurred.')
# print("Out of try except blocks.")

# try:
#     a=5
#     b='0'
#     print (a+b)
# except TypeError:
#     print('Unsupported operation')
# print ("Out of try except blocks")

# a=5
# b='0'
# print (a+b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
#
# try:
#   print(x)
# except:
#   print("An exception occurred")

# l=[1,2,3,4,5]
# print(l[7]) #IndexError: list index out of range

try:
    l = [1, 2, 3, 4, 5]
    print(l[7])
except IndexError:
    print("indexerror")
    import sys
    print(sys.exc_info())
# finally:
#     print("MMMMMMMMMMMMMMMMMMMMMMMM")
