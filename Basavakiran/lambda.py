# TO FIND SUM OF 2 NUMBERS USING LAMBDA WITHIN FUNCTION
def sum():
    y=lambda a,b:a+b
    print(y(2,4))
sum()
#
# TO FIND SUM OF 2 NUMBERS USING ONLY LAMBDA
a=int(input('enter the value of a : '))
b=int(input('enter the value of b : '))
c=[]
x=lambda a,b:a**b
# print(x(a))
c.append(x(a,b))
print(c)

# TO FIND SQUARE OF A NUMBER USING LAMBDA WITHIN THE FUNCTION
def dk(a):
    x=lambda a:a*a
    print(x(a))
dk(2)
