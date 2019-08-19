# def file_read(fname):
#     txt = open(fname)
#     print(txt.read())
#
# file_read('../file.txt')


# def file_read(fname):
#     with open(fname, "a") as myfile:
#        myfile.write("Python Exercises\n")
#        txt = open(fname)
#     print(txt.read())
# file_read('../file.txt')
#

# def file_read(fname):
#     with open(fname) as f:
#         a = f.readlines()
#         print(a)
# file_read('../file.txt')

# list=['hello','doctpr']
# f=open('ttt.txt','r')
# # f.writelines(list)
# a=f.readlines()
# print(a)


#example for seek() & tell()
# data="hi good morning"
# f=open('../nivya.txt','w')
# f.write(data)
# f =open('../nivya.txt','r+')
# txt = f.read()
# print(txt)
# print('the current position:', f.tell())
# f.seek(17)
# print(f.tell())
# f.write('Good evening')
# f.seek(19)
# text = f.read()
# print("data after modification")
# print(text)

# WAP to check whether the given file exists or not. If avaliable then print its content?
# import os
# fname=input(('enter filename:'))
# if os.path.isfile(fname):
#     print('File Exists:',fname)
#     f=open(fname,'r')
#     print('the content of the file is:')
#     print(f.read())

# WAP to get the number of lines, words and character are there in a file
import os
fname=input(('enter filename:'))
if os.path.isfile(fname):
    print('File Exists:',fname)
    f=open(fname,'r')
    lcount=wcount=ccount=0
    for i in f:
        lcount=lcount+1
        words=i.split()
        wcount=wcount+len(words)
        ccount=ccount+len(i)
    print(lcount)
    print(wcount)
    print(ccount)
else:
    print('file does not exist')