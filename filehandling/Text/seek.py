f=open('niv.txt','a')
f.write("hello Nivya\n")
f.write("hello Akash\n")
f.write("hello Blaster\n")
f.close()

print(f.seek(12))        #12
print(f.read(3))         #hel
print(f.seek(3))         #3
print(f.read(7))         #lo Nivy


