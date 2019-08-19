f=open('niv.txt','w')
f.write("hello Nivya\n")
f.write("hello Akash\n")
f.write("hello Blaster\n")
f.close()

f=open('niv.txt','r')
print(f.tell())          #0
print(f.read(2))         #he
print(f.tell())          #2
print(f.read(3))         #llo
print(f.tell())          #5
print(f.read(5))         #nivy
print(f.tell())          #38
