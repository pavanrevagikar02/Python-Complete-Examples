#
# # list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# a = set()
# for i in [2, 3, 4, 4, 5,8, 6, 6]:
# 	if i % 2 == 0:
# 		a.add(i)
# print(a)
#
# # # # Using Set comprehensions
# # list= [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# # a= {i for i in list if i % 2 == 0}
# # print(a)
#
# '============================='
# a= set()
# for x in [10,20,30]:
#     for y in [2, 4, 6]:
#         a.add(x*y)
# print(a)
# # #
# # #set comprehensions
# a={x*y for x in [10,20,30] for y in [2,4,6]}
# print(a)
#
# a=set()
# for i in range(1,6):
#     a.add(i**2)
# print(a)
#
# a={i**2 for i in range(1,6)}
# print(a)
#
# a=set()
# for i in range(10):
#     if(i%2==0):
#         a.add(i)
# print(a)
#
# a={i for i in range(10) if i%2==0}
# print(a)