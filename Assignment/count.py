data="pavan123"
d=0
l=0
for x in data:
    if x.isalpha():
        l=l+1
    else:
        x.isdigit()
        d=d+1
print("Letter:", l)
print("Digit:", d)

# 'patterns'
#
# n=3
# for i in range(0,n):
#     for j in range(i):
#         print('*',end="")
#     print(' \n ')