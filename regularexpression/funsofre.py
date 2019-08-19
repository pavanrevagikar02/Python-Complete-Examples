import re
x=re.compile('python')
print(type(x))
matcher=x.finditer('learning python is easy')
for i in matcher:
    print(i.start())
    print(i.end())

import re
count=0
x=re.compile('ab')
y=x.finditer('abaababa')
for i in y:
    count = count + 1
    print(i.start())
print("The no of occurance of the pattern:", count)

# import re
# count=0
# y=re.finditer('aa','abaababa')
# for i in y:
#     count = count + 1
#     print("start:{},end:{},group:{}".format(i.start(),i.end(),i.group()))
# print("The no of occurance of the pattern:", count)

# import re
# count=0
# y=re.finditer('7','11abaaba77b77a')
# for i in y:
#     count = count + 1
#     print("start:{},end:{},group:{}".format(i.start(),i.end(),i.group()))
# print("The no of occurance of the pattern:", count)

