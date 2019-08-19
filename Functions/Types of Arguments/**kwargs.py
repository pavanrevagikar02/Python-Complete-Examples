# #  keyword variable length argument
# def test(**kwargs):
#      print(type(kwargs))
# test(s_name="tom", s_id=20,s_addr="mysore")
#
# def test(**kwargs):
#     print("student details")
#     # print(type(kwargs))
#     for k,v in kwargs.items():
#         print(k,':', v)
# test(s_name="tom", s_id=20,s_addr="mysore")
#
#
# def intro(**data):
#     print("\nData type of argument:",type(data))
#     for key, value in data.items():
#         print("{} is {}".format(key,value))
# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


def test(*a,**b):
    print(a[1]+b['b']+b['c'])
test(10,20,b=20,c=8)