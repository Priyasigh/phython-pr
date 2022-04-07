p = [10,20,15,20,20,60,55]
u=[]

count=0
for i in p:
    if i not in u:
        u.append(i)
        count=count+1

print("unique:",count)
print(u)