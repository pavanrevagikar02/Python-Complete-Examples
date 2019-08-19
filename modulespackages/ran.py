import random
print(random.random())
print(random.randint(1,100))
print(random.choice('computer'))
print(random.randrange(0,101,10))
#
# num=[1,2,45,7]
# random.shuffle(num)
# print(num)


# import random
# print(random.choice('computer'))
# print(random.choice([12,23,'hi',43]))
#print(random.choice((12,23,45,67,65,43)))

import random
numbers=[12,23,45,67,65,43]
strg=['hello','ell','ehco']
random.shuffle(numbers)
random.shuffle(strg)
print(numbers)
print(strg)