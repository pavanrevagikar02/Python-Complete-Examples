# output_list = [output_exp for var in input_list if (var satisfies this condition)]
# Syntax
# list_variable = [x for i in iterable]

# List Comprehension vs For Loop
#
# Constructing output list using for loop
# list = []
# for i in range(1, 10):
#     list.append(i ** 2)
# print(list)
#
# # Using List comprehensions
# a=[i**2 for i in range(1,10)]
# print(a)

# using for loop
# list=[]
# for i in 'developer':
#     list.append(i)
# print(list)
#
# #Using List comprehensions
# a=[i for i in 'developer']
# print(a)

# #  List comprehensions with conditional expression
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in a:
#     if(i%2==0):
#         b.append(i)
# print(b)
#
# # # Using List comprehensions
# a=[1,2,3,4,5,6,7,8,9,10]
# b= [i for i in a if i % 2 == 0]
# print(b)
#
# The numbers less than 100, which are divisible by 2 and 5 both.
# using for loop with nested conditions

# list=[]
# for i in range(100):
#     if((i%2==0) and (i%5==0)):
#         list.append(i)
# print(list)

# # Nested IF with List Comprehension
#
# a=[x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# print(a)
#
# fishtypes= ['blowfish', 'octopus', 'clownfish', 'catfish']
# x= [i for i in fishtypes if i!= 'octopus']
# print(x)

# if ...else With List Comprehension
a = [i if i%2==0 else "odd" for i in range(10)]
print(a)
#
# for loop using
for i in range(10):
    if i%2==0:
        print('even')
    else:
        print("odd")

#Nested for
list = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        list.append(x * y)
print(list)
#
a=[x*y for x in [20,40,60] for y in [2,4,6]]
print(a)
#
#
