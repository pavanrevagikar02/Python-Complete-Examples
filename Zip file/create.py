from zipfile import *
f=ZipFile('myfile.zip','w',ZIP_DEFLATED)
f.write('/home/nivya/Inventateq Python/basics prgm/control statements.py')
f.close()