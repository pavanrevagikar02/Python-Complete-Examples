# f=open('../xyz.txt','w')
# tuple=('hello\n','how\n', 'are\n','you\n')
# f.writelines(tuple)
# f.close()
#
#
# f=open('xyz.txt','w')
# tuple=('hello\n','how\n', 'are \nyou')
# f.write(tuple)  #TypeError: write() argument must be str, not tuple
# f.close()

#read()

# f=open('../xyz.txt')
# data=f.read()
# print(data)
# f.close()

#read(args)

# f=open('../xyz.txt')
# print(f.read(3))
# f.close

#readline()

# f=open('../xyz.txt','r')
# first=f.readline()
# print(first,end='')
# second=f.readline()
# print(second)
# f.close()


# f=open('../xyz.txt','w')
# list=("hello\n","good morning\n", "to\n", "python\n", "class\n")
# f.writelines(list)
# f.close()

# f=open('../xyz.txt','r')
# x=f.readlines()
# print(x)

f=open('../xyz.txt','r')
x=f.readlines()
for i in x:
    print(i,end='')
f.close()

with open('../xyz.txt','r') as f:
    data = f.readlines()

for line in data:
    words = line.split()
    print(words)


# f=open('xyz.txt','r')
# s=f.read(10)
# print(s)

# f = open('my_file', 'w+b')
# byte_arr = [120, 3, 255, 0, 100]
# binary_format = bytearray(byte_arr)
# f.write(binary_format)
# f.close()
