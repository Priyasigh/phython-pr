import csv

file=open("details.csv","r")
type(file)
csvreader= csv.DictReader(file)
header=next(csvreader)
print(header)

rows=[]
for row in csvreader:
    rows.append(row['city'])
print(rows)
a=0
m=0

for i in rows:
    if i=='ahemedabad':
        a=a+1
    elif i=='mehsana':
        m=m+1
print(f"ahmedabad:{a},mehsana:{m}")
file.close()


