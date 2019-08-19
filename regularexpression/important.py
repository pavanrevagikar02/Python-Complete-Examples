#match()
# import re
# s=input("enter pattern to check:")
# matcher=re.match(s,'abcdefgh')
# if matcher!=None:
#     print("match is avaliable")
#     print('startindex:{} and groupindex:{}'.format(matcher.start(),matcher.group()))
# else:
#     print("match not is avaliable")

# There are the following methods associated with the Match object.
# span(): It returns the tuple containing the starting and end position of the match.
# string(): It returns a string passed into the function.
# group(): The part of the string is returned where the match is found.

#fullmatch()
# import re
# s=input("enter pattern to check:")
# matcher=re.fullmatch(s,'abcdefgh')
# if matcher!=None:
#     print("fullmatch is avaliable")
#     print('startindex:{} and endindex:{}'.format(matcher.start(),matcher.group()))
# else:
#     print("fullmatch not is avaliable")

#search()
# import re
# s=input("enter pattern to check:")
# matcher=re.search(s,'abcdefgh')
# if matcher!=None:
#     print("fullmatch is avaliable")
#     print('startindex:{} and endindex:{}'.format(matcher.start(),matcher.group()))
# else:
#     print("fullmatch not is avaliable")

# import re
# l=re.findall('[0-9]','a7b9k6z')
# print(l)
#
# import re
# l=re.findall('\w','a7#')
# print(l)

# import re
# str = "Life is really simple, but we insist on making it complicated."
# matches = re.search("is", str)
# print(type(matches))
# print(matches)  # matches is the search object
#
# import re
# str = "How are you. How is everything"
# matches = re.search("Life is really simple, but we insist on making it complicated", str)
# print(matches.span())
# print(matches.group())
# print(matches.string)

# sub(): The sub() function replaces the matches with the text of your choice:

#Replace all white-space characters with the digit "9":

# import re
# a = "There are no shortcuts to any place worth going"
# x = re.sub("\s", "9",a)
# print(x)
#
# # You can control the number of replacements by specifying the count parameter:
# import re
# a = "There are no shortcuts to any place worth going"
# x = re.sub("\s", "9",a,2)
# print(x)
#
# import re
# s=re.sub('\d','#', 'a8b9klo4u')
# print(s)

# subn()
# import re
# t=re.subn('\W', '~*' , 'Subject has Uber booked already')
# print(t)
# print(t[0],t[1])
# print(t[0])
# print(t[1])


# import  re
# t=re.subn('\d',"$", 'a8klpfg7f7dh9')
# print(type(t))
# print('The result string is',t[0])
# print('No of replacements ',t[1])

# split()

import re
l=re.split('\W+', 'Words, words , Words')
print(l)
k=re.split('-', '10-20-30-56-100')
print(k)
t=re.split('\.','www.yahoo.com')
for x in t:
    print(x)

