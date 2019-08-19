# TO GET THE EVEN NUBERS
# a=int(input('enter the value in btw 0 to 10 '))
# def even(a):
#     for i in range(0,a):
#         if (i%2==0):
#             print(i)
# even(a)

# TO GET THE EVEN NUBERS USING FUNCTION
# a=int(input('enter the velue in btw 0 to 10 '))
# x=[]
# def even(a):
#     for i in range(0,a):
#         if (i%2==0):
#             # print(i)
#             x.append(i)
#     print(x)
# even(a)

# TO GET THE EVEN NUBERS USING FILTER WITH LAMBDA
# a=int(input('enter the velue in btw 0 to 10 '))
# a=range(0,20)
# x=list(filter(lambda a:(a%2==0),range(0,10)))
# print(x)

# MULTIPLICATION OF 2 LISTS
# l1=[1,2,3,4,5,6,7]
# x=len(l1)
# l2=[2,3,6,7,8,9,1]
# l3=[]
# for i in range(0,x):
#     # print(l1[i]*l2[i])
#     l3.append(l1[i]*l2[i])
# print(l3)

# MULTIPLICATION OF 2 LISTS USING MAP WITH LAMBDA
# l1=[1,2,3,4,5,6,7]
# l2=[2,3,6,7,8,9,1]
# x=list(map(lambda a,b:a*b,l1,l2))
# print(x)

# FINDING SQUARE OF A NUMBER
# a=int(input('enter a number : '))
# def sqr(a):
#     print(a**2)
# sqr(a)

# FINDING SQUARE OF A LIST OF NUMBERS USING LAMBDA
# l1=[1,2,3,4,5,6]
# x=list(map(lambda a:a**2,l1))
# print(x)

# FINDING SQUARE OF A LIST OF NUMBERS OR RANGE USING MAP WITHIN THE FUNCTION
# l1=range(1,10)     # OR
# # l1=[1,2,3,4,5,6,7,8,9]
# def sqr(l1):
#     return l1**2
# x=list(map(sqr,l1))
# print(x)

# FINDING SQUARE OF A LIST OF NUMBERS USINGLAMBDA,MAP WITHIN THE FUNCTION
# l=[1,2,3,4,5,6,7,8,9]
# def sqr(l1):
#     return l1**2
# x=list(map(lambda l1:l1**2,l))
# print(x)

# MULTIPLICATION TABLE USING LAMBDA
# m=int(input('enter the number : '))
# def mul(m):
#     return lambda a:a*m
# b=mul(m)
# for i in range(1,11):
#     print(b(i))

# MULTIPLICATION TABLE
# m=int(input('enter the number : '))
# for i in range(1,11):
#     print(m,'*',i,'=',m*i)







