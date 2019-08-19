# int()
# a=int(10.123)
# # a=int(10+2J) # TypeError: can't convert complex to in
# a=int(True)
# a=int(False)
# a=int("10")
# a=int("10.5") # ValueError: invalid literal for int() with base 10: '10.5'
# print(a)



#float()

a=float(10)
print(a)
# a=float(20+20J) # TypeError: can't convert complex to in
print(a)
a=float(True)   #1.0
print(a)
a=float("10.5")
print(a)
a=float('10')
print(a)
#
# # complex()
a=complex(10)
print(a)
a=complex(10.5+0j)
print(a)
a=complex(1+0J)
print(a)
a=complex("10")
print(a)
a=complex("10+0J")
print(a)
#
# #bool()
a=bool(10)
print(a)
a=bool(0.1)
print(a)
a=bool(0+1j)
print(a)
a=int("10")
print(a)
a=bool(" ")
print(a)

#
#
# #str()
a=str(10)
print(a)
print(type(a))
a=str(10.5)
print(a)
a=str('true')
print(a)
a=str(10+20J)
print(a)

