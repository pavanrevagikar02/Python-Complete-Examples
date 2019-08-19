# WAP TO CHECK WHETHER THE GIVEN FILE EXISTS OR NOT IF AVALIABLE THEN PRINTITS CONTENT
#
# import os
# f=input("enter your name:")
# if os.path.isfile(f):
#     print("file  exist:",f)
#     f=open(f,'r')
#     print('print the content of the file')
#     print(f.read())
# else:
#     print("file doesnt exist")

# import os
# f='nivs.txt'
# if os.path.isfile(f):
#     print("file  exist:",f)
#     f=open(f,'r')
#     print('print the content of the file')
#     print(f.read())
# else:
#     print("file doesnt exist")

#CHECK IF FILE EXIST:

# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# import os
# if os.path.exists("xyz.txt"):
#   os.remove("xyz.txt")
# else:
#   print("The file does not exist")

# WAP an print the no of lines , words nd character are there n a file.
#
# import os
# f=input("Enter the file Name:")
# if os.path.isfile(f):
#     print(f)
#     f=open(f,'r')
#     lc=wc=cc=0
#     for i in f:
#         lc=lc+1                     # no of lines
#         words=i.split()            # no of words
#         wc=wc+len(words)
#         cc=cc+len(i)                #no of characters
#     print(lc)
#     print(wc)
#     print(cc)
# else:
#     print("File not exixts")
#

#
# s="hello welcome to python class"
# l=s.split()
# print(l)

#
# f=open('../abc.txt','r')
# lc=wc=cc=0
# for i in f:
#     lc=lc+1                     # no of lines
#     words=i.split()            # no of words
#     wc=wc+len(words)
#     cc=cc+len(i)                #no of characters
#     print("no of lines:",lc)
#     print("no of words:",wc)
#     print(" no of characters:",cc)

import os
x=input("enter the txt file:")
if os.path.exists(x):
  os.remove(x)
else:
  print("The file does not exist")
