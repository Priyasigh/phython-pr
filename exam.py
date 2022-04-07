import csv
import pandas as pd

rollno = []
studname = []
sub1 = []
sub2 = []
sub3 = []
total = []
per = []
i  = int(input("Enter no. of students:-\n"))
header = ['Rollno', 'studname', 'sub1', 'sub2', 'sub3', 'total', 'per']
with open('marks.csv', 'a', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
for x in range(0, i ):
    print(f"\n\n\nEnter details for student {x+1}\n")
    r1 = int(input("Enter roll no:-"))
    n1 = input("Enter Name:-")
    s1 = int(input("Enter marks of subject 1:-"))
    s2 = int(input("Enter marks of subject 2:-"))
    s3 = int(input("Enter marks of subject 3:-"))
    rollno.append(r1)
    studname.append(n1)
    sub1.append(s1)
    sub2.append(s2)
    sub3.append(s3)
    total.append(s1 + s2 + s3)
    per.append((s1 + s2  + s3)/3)
    data = [rollno[x],studname[x],sub1[x],sub2[x],sub3[x],total[x],per[x]]
    with open('marks.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)   
for x in range(0, i):
    print(f"\nRoll no. {rollno[x]}, {studname[x]} has scored {sub1[x]},{sub2[x]},{sub3[x]} in subject1, subject2 and subject3 repectively, with a total of {total[x]}and generating a percentage of {per[x]}")
csvdata = pd.read_csv("marks.csv")
csvdata.sort_values(["per"], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)
print("end")