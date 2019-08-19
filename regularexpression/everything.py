# #Findall
# import re
# x = "python3 is easy to learn"
# r = re.findall("\w",x)
# print(r)
# #
# # import re
# # a = re.findall("i", "We need to inform him about the timings!")
# # for i in a:
# #     print(i)
#
# import re
# str = "python3,is easy to learn and easy to do programming"
# x = re.findall("easy", str)
# print(x)
# #
# #finditer()
#
import re
Str = "we need to inform him with the latest information"
for i in re.finditer("inform.", Str):
    print(i.span())
#
# # search()
# import re
# str = "python3 is easy to learn"
# x = re.search("\s", str)
# print("The first white-space character is located in position:", x.start())
#
# import re
# if re.search("inform", "we need to inform abt the timings"):
#     print("There is inform")
# else:
#     print("There is no inform")
#
# # import re
# # x = "software develeoper in techpark"
# # print(re.search('techpark', x))