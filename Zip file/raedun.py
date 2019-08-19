# # # to check the list of files in the zip files
# from zipfile import *
# f=ZipFile('myfile.zip','r',ZIP_STORED)
# names=f.namelist()
# for i in names:
#     print(i)
#     f1=open(i,'r')
#     print(f1.read())
# print('===========================')


from zipfile import *
f=ZipFile('files.zip','r',ZIP_STORED)
names=f.namelist()
for i in names:
    print(i)
    print('the content of this file is:')
    f1=open(i,'r')
    print(f1.read())
    print('*'*10)



