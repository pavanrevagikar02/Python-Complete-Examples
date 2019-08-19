# try-except with else block
# The except statement with no exception
try:
    l = []
    a = lambda x, y: x + y
    l.append(a(10, 20))
    print(l)
except:
    print("The except statement with no exception")
else:
    print("No Exception")

# try:
#     #this will throw an exception if the file doesn't exist.
#     f = open("file.txt","r")
# except IOError:
#     print("File not found")
# else:
#     print("The file opened successfully")
#     f.close()

