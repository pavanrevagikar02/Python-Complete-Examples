# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

# # Using loop for constructing output dictionary
a= [1, 2, 3, 4, 5]
b={}
for i in a:
	if i% 2 != 0:
	 b[i]=i**3
print(b)

# # Using Dictionary comprehensions
# # for constructing output dictionary
#
# a = [1,2,3,4,5]
# b= {i: i ** 2 for i in a if i % 2 == 0}
# print(b)

# # Using loop for constructing output dictionary
xdict={}
subject = ['Kannada', 'Maths', 'English']
marks = [90, 80, 89]
for (key, value) in zip(subject, marks):
	xdict[key] = value
print(xdict)

# a={'Kannada': 90, 'Maths': 80, 'English': 89}
# a['cs']=50
# print(a)

# Using Dictionary comprehensions for constructing output dictionary
# Syntax: [xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
subject = ['Kannada', 'Maths', 'English']
marks = [90, 80, 89]
a = {key:value for (key, value) in zip(subject,marks)}
print(a)

# Using loop for constructing output dictionary
dict={}
a=[1,2,3,4,5]
b= [90, 80, 89]
for (key, value) in zip(a, b):
	dict[key] = value
print(dict)

# Dictionary comprehensions
a=[1,2,3,4,5]
b= [90, 80, 89]
x={k:v for k,v in zip(a,b)}
print(x)