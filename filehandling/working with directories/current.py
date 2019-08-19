import os
# cwd=os.getcwd()
# print(cwd)

# os.mkdir('hello/hi')
# print('successful')

# os.makedirs('king/queen/prince')
# print('successful')
#
# os.rmdir('hello/hi')
# print("removed sucessfuly")

# os.removedirs('king/queen/prince')
# print("removed sucessfuly")

# os.rename('hello','myfolder')
# # print("removed sucessfuly")

print(os.listdir('.'))
list=os.listdir()
for name in list:
    print(name)

# list=os.listdir("/home/nivya/Inventateq Python")
# for name in list:
#     print(name)
# print(len(list))