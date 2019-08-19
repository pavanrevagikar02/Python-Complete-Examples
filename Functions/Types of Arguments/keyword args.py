# keyword Argument
def test(empid,empname):
    print(empid)
    print(empname)

test(empid =12,empname="kiran")
# test("101",empname="akash") #func() got multiple values for argument 'name'
# test(empname="pavan", "776") #positional argument follows keyword argument
test(7,empid=89)


# def cal(a,b):
#     print(a+b)
# cal(a=100,b=50)
    # cal(a=50,100)   # positional argument follows keyword argument
    # cal(a=100,b=50)


