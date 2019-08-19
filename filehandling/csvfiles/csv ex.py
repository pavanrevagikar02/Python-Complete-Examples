import csv
with open('student.csv','w',newline='')as f:
    a=csv.writer(f)
    a.writerow(['NAME','ID','MARKS','ADDRESS'])
    while True:
        name=input("enter s_name:")
        id=int(input("enter s_id:"))
        marks=int(input("enter s_marks:"))
        addr=input("enter s_addr:")
        a.writerow([name,id,marks,addr])
        option=input('Do you want to insert one more record[Yes|No]:')
        if option.lower()=='no':
            break
print("students data inserted to csv file sucessfully")