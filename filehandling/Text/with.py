# with open('abc.txt','w')as f:
#     f.write('hello\n')
#     f.write('doctor\n')
#     f.write('meena\n')
#     print(f.closed)
# print(f.closed)

with open('abc.txt', 'r') as f: #open the file
    contents = f.readlines()
f.close()
print(contents[2],"@@@@@@@@")
