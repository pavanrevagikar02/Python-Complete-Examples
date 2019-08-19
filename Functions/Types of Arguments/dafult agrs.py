# default agruments
def me(name,salary="25k"):
    print("My name is",name)
    print("my sal is:",salary)
me("xyz")
#the variable salay is not passed into the function however the default value of salary is considered in the function
#
def sum(a=1,b=30):
    print(a+b)
sum(a=30,b=40)

def me(name,age=22):
    print(name,age)
me(name = "akash") #the variable age is not passed into the function however the default value of age is considered in the function
me(age = 10,name="pavan") #the value of age is overwritten here, 10 will be printed as age
