a=10
print(a)

# # The actual syntax of the print() function is
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Here, objects is the value(s) to be printed.
#
# The sep separator is used between the values. It defaults into a space character.
#
# After all values are printed, end is printed. It defaults into a new line.
#
# The file is the object where the values are printed and its default value is sys.stdout (screen).

print('hello','good morning',10,90)

print(1,2,3,4,sep='*')

print(1,2,3,4,sep='#',end='\n')

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y)) #The value of x is 5 and y is 10

print('Hello {name}, {message}'.format(message = 'Goodmorning', name = 'Akbar'))