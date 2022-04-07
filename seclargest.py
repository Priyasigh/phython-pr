p = [10,20,15,60]
print(p)

temp=0
for i in range(0,len(p)):
    for j in range(i+1,len(p)):
        if(p[i]>p[j]):
            temp=p[i]
            p[i]=p[j]
            p[j]=temp
print("second largest:",p[-2])