# creating dictonary
# d = {'name': 'nivya', 'age': 80}
# print(d)

# Acessing values in dict [key]
d = {'name': 'nivya', 'age': 80}
print(d['age'])

# updation of values
d['salary'] = 100000
print(d)

d['age'] = 20
print(d)

x = 'developer'
d['profession'] = x
print(d)

# Deletion
del d['salary']
print(d)
# del d
# print(d)

# Length
print(len(d))

# to get oly keys
print(d.keys())

# to get oly values
print(d.values())

# to get both key-values
print(d.items())

# update
# data1 = {'salary': 28000, 'name1': 'shreyas'}
# d.update(data1)
# print(d)

# data = {1:{'salary': 28000, 'name1': 'shreys'},
#         2:{'Name2':2999,'sid':20}}
# print(data)

# Nested Dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people[1]['name'])
print(people[1]['age'])
print(people[2]['sex'])

#clear
d.clear()
print(d)

# copy()
x={'sub':"maths",'marks':8}
y=x.copy()
print(y)
print(x)

# to get only keys
print (x.get('marks'))
print (x['marks'])

Dict = {'a':1,'b':2,'c':3,'d':4}
# print(Dict)
if 'a' in Dict:
    del Dict['a']
print(Dict)















