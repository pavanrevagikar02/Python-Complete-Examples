# f=open('test.txt','w')
# f.write("hello Nivya\n")
# f.write("hello Akash\n")
# f.write("hello Blaster\n")
# f.close()


f1=open('test.txt','r')
f2=open('test1.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print('Sucessfully copied')
