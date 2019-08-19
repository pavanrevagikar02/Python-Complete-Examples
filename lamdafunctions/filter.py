# # prime number
# # def prime(x):
# #     for n in range(2,x):
# #         if x%n==0:
# #             return False
# #         else:
# #             return True
# #
# # test=list(filter(prime,range(0,10)))
# # print(test)
#
#
#
# # to print even numbers from 1 to 10 using normal function
#
# def display():
#     for i in range(1,10):
#         if(i%2==0):
#             print(i)
# display()
#
#
# l=[]
# def display():
#     for i in range(0,10):
#         if i%2==0:
#             l.append(i)
#     print(l)
# display()
#
# # # program returns a list of even numbers from a range.
# data=(lambda x: x%2==0, range(10)) # (<function <lambda> at 0x7f8095cd1378>, range(0, 10))
# data1=filter(lambda x: x%2==0, range(10)) #<filter object at 0x7f14a408ccf8>
# data2=list(filter(lambda x: x%2==0, range(10))) #<filter object at 0x7f14a408ccf8>
# print(data)
# print(data1)
# print(data2)
#
# # l=[1,2,3,4,5,6,6,8,9,10]
# # data=list(filter(lambda x: x%2==0,l))
# # print(data)
# #
# # square=[1,2,3,4,5,6,7]
# # h=list(filter(lambda x:x*x,square))
# # print(h)
#
# #
# # # prgm is to append a even number to empty list
# # def test(l):
# #     data = []
# #     for i in l:
# #         if i % 2 == 0:
# #             data.append(i)
# #     return data
# # print(test(range(10)))

# Function to find intersection of two arrays

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

def interSection(arr1,arr2):

	# filter(lambda x: x in arr1, arr2) -->
	# filter element x from list arr2 where x
	# also lies in arr1
	result = list(filter(lambda x: x in arr1, arr2))
	print ("Intersection : ",result)

interSection(arr1,arr2)
