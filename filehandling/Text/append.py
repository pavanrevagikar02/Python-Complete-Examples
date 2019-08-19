f=open("abc.txt",'w')
list=["hello\n",'good morning\n',
      'welcome\n',
      'to\n',
      'python\n'
      'class\n']
f.writelines(list)
f.close()
f=open('abc.txt','a')
f.write("something")
f=open('abc.txt','w')
f.write("Nivya")
f.close()
