# import csv
# with open('student.csv','r')as f:
#     r=csv.reader(f)
#     data=list(r)
#     print(data)         # returns in nested list

# import csv
# with open('student.csv', 'r')as f:
#     r = csv.reader(f)
#     data = list(r)
#     for row in data:
#         print(row)         # returns data in the form of list

    #
    # data=list(r)
    # for row in data:
    #     for column in row:
    #         # print(column)       # returns one by one
    #         # print(column,end='')    #NAMEIDMARKSADDRESSnivya287Bangalorelikith389Hyd
#     #         print(column,'\t',end='')
import csv
with open('student.csv', 'r')as f:
    r = csv.reader(f)
    data=list(r)
    for row in data:
        print(row[0],row[1],row[2],sep='\t\t')

