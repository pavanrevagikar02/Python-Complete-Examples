# # Mobile number validation
# import re
# s=input("enter pattern to check:")
# m=re.fullmatch('[6-9]\d{9}',s)
# if(m!=None):
#     print(s,'is valid mobile no')
# else:
#     print(s,'is valid NOT mobile no')
#
# # Email Validation
#
# import re
# a=input("Enter the email to validate: ")
# m=re.fullmatch('[\w]+[@]{1}[a-z]+[\.]{1}[a-z]+',a)
# if m!=None:
#         print(a, "is a valid Email")
# else:
#     print(a,"is an Invalid email")

# Identifier validation

# import re
# s=input("enter Identifier to validate:")
# m=re.fullmatch('[a-k] [0369][a-zA-Z0-9#]*',s)
# if m!=None:
#     print(s,'is a valid Identifier')
# else:
#     print(s, 'is a not valid Identifier')

# import re
# f1=open('abc.txt','r')
# # f1.write("9916961090")
# f2=open('xyz.txt','w')
# for line in f1:
#     list=re.findall('[6-9]\d{}',line)
#     for num in list:
#         f2.write(num)
# f1.close()
# f2.close()