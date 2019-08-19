# Position arguments
def test(a,b):
    print("hello good morning")
test(100,50)
test(100,78)

def test(a,b):
    test(100, 50)
    test(50, 100)
print("hello good morning")


def cal(a,b):
    sum=(a+b)
    return sum
x=cal(100,7)
print(x)

# def cal(a,b):
#     sum=(a+b)
#     return sum
# x=cal(100)
# print(x) #cal() missing 1 required positional argument: 'b'