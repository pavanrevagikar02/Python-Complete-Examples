import csv
with open('student.csv','r+')as f:
    r=csv.reader(f)
    w=csv.writer(f)
    data=list(r)
    for row in data:
        if row[0]=="nivya":
            w.writerow([row[0],100,row[2],row[3]])