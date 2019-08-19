def display(*args):
    print("single aguments")
display(10,20)
display(10,20,45)
display(10,20,88,000,888)

def cal(*args):
    n=1
    for i in args:
        n=n*i
        print(n)
cal(10,60)
cal(100,60)

def call(**args):
    for i in range(1,10):
        print(i)
call(a=10,b=20,c=10)

def sum(*args):
    for arg in args:
        print(arg)

# print('sum(10, 20)')
sum(10, 20)
# print('sum(10, 20, 30)')
sum(10, 20, 30)
# print('sum(10, 20, 30, 40)')
sum(10, 20, 30, 40)