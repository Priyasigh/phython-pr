import csv
file=open("Book1.csv","r")
read=csv.reader(file)
s=0
a=[]
b=[]
c=[]
max=0
for i in read:
    a.append(i)

for i in range(0,len(a)):
    s=0
    for j in range(0,len(a[i])):
        if(j != 0):
            s=int(a[i][j])+s
    b.append(s)
    
for i in range(0,len(b)):
    print(i+1,"percentage:",b[i]/4)
    c.append(b[i]/4)
    for i in c:
        if i>max:
            max=i

print(f"Eno is a ranker having {max} percentages")

    