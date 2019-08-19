# # variable declared inside the class
# def print_message():
#     message = "hello !! I am going to print a message." # the variable message is local to the function itself
#     print(message)
# print_message()
# # print(message)
#
#
# #variable declaed outside the class

def calculate(*args):
    sum=0
    for arg in args:
        sum = sum +arg
    print("The sum is",sum)
sum=0
calculate(10,20,30) #60 will be printed as the sum
print("Value of sum outside the function:",sum) # 0 will be printed

#
# total = 30
# def sum( a,b):
#    # Add both the parameters and return them."
#    total = a + b; # Here total is local variable.
#    print ("total : ", total)
#    return total;
#
# # Now you can call sum function
# sum( 10, 20 );
# print(total)
#
# a=10 # Global Variable
# def f1():
#     a=20 # Local Variable
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()
#
# # Global keyword
# a=10 # Global Variable
# def f1():
#     global a  # Global keyword
# # to bring global variable to the function for the required modification
#     a=20 # we are changing the value of global variable
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()
# # to make GV avaliable to the function so that we can perform required modification

# a=10 # Global Variable
# def f1():
#     a=20 # Local Variable
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()