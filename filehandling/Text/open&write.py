
# Write()
# f=open("../abc.txt",'w')
# f.write("n good night")
# f.close()

#Writelines()

# f=open("abc.txt",'w')
# list=["hello\n",'good morning\n',
#       'welcome\n',
#       'to\n',
#       'python\n'
#       'class\n']
# f.writelines(list)
# print("All the lines from the list written to the file")
# f.close()

# f=open("../hello/abc.txt",'w')
# # data={'name:nivya\n','id:ydgdh\n'}
# # f.writelines(data)
# f.write("nivya")  #overwritten

# write to txt using exception

# try:
#     f = open("../demofile3.txt", "w")
#     f.write("Woops! I have deleted the content!")
# except:
#     import sys
#     print(sys.exc_info())
# finally:
#     f.close()
