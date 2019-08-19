# To create and write
# f=open("../new/abc.txt",'a')
# f.write('wel come to python \n')
# f.write('Blaster Basavakiran \n')
# f.write('thank you')

# To get output
# f=open("abc.txt")
# print(f.read())

# To delete file
# import os
# os.remove("abc.txt")

# For list we must and should nead writeline instead of write
# f=open("xyz.txt",'w')
# list=['hi','hello','basava']
# f.writelines(list)


################# NOTE: w+ : write + read , r+ : read + write , a+ : append + read

# f.writelines("gm")
# f.close()
# f=open("basava.txt",'a')
# f.writelines('hello')

## f=open("zxc.txt",'r+')
## print(f.read())
## f.write('Basava')


# To check so conditions
# f=open("xyz.txt",'w+')
# f.write('nivya')
# f.seek(0)
# print(f.read())
# print("name",f.name)
# print("mode",f.mode)
# print("writable",f.writable())
# print("readable",f.readable())
# # f.close()
# print("closed",f.closed)





f=open('abc.txt','w')
list=['hi','hello','python']
f.writelines(list)
print("all the lines from the list written to the file")
f.close()


