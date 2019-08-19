# #A new empty set
# x= {1,35635,"ttyetfu"}
# print(x)

# A non empty set
# n = set([0, 1, 2, 6, 3, 4, 5])
# print(n)

# #set method
# n=set([1,2,77,3,4,4,44])
# print(n[0]) #TypeError: 'set' object does not support indexing

#add()
# n={1,2,'ooso','iiiii'}
# n.add('reshma')
# print(n)

#update()
# x= {"apple", "banana", "cherry"}
# x.update(["orange", "mango", "grapes"])
# print(x)

# length of set

# x={'apple', 'mango', 'grapes', 'orange', 'cherry', 'banana'}
# print(len(x))

#remove the item from the set

# x={'apple', 'mango', 'grapes', 'orange'}
# x.remove('apple')
# print(x)

#clear()
# x={'apple', 'mango', 'grapes', 'orange'}
# x.clear()
# print(x)

# delete

# a={1,2,3,4,5}
# del a
# print(a) #this will raise an error because the set no longer exists

# #intersection
# sx={1,2,3,4,5}
# sy={1,4,5,3,9,8}
# sz=sx&sy
# print(sz)

# #Union
sx={1,2,3,4,5}
sy={1,4,5,3,9,8}
sz=sx|sy
print(sz)
#
# #difference
sx={1,2,9,4,5}
sy={1,2,4,8,5,4}
sz=sx-sy
print(sz)

# #Shallow copy of sets
# setx = set(["orr", "blue"])
# sety = set(["blue", "green"])
# #A shallow copy
# setd = setx.copy()
# print(setd)
#
# # copy()
# h={'mon','tue', 'wed'}
# a=h.copy()
# print(a)


# #discard()
# h={'mon','tue','wed'}
# h.discard()
# print(h)

#isdisjoint()

sx={1,2,9,4,5}
sy={3,8,45}
sz=sx.isdisjoint(sy)
print(sz)

#issubset()
sx={1,2,3,4}
sy={9,8,1,2,3,4}
sz=sx.issubset(sy)
print(sz)

#pop()
sx={2,3,1,4,5}
sx.pop()
print(sx)

sx={1,2,3,4}
sy={9,8,1,2,3,4}
sz=sx.symmetric_difference(sy)
print(sz)

