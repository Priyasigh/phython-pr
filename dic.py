'''
 write a python code to store eno and percentage of 5 students in 
 python dictionary and find print the ranker student with his/her eno and percentage.
'''
per={"1001":50.56,"1002":90.65,"1005":9.20,"1003":45.68,"1004":80.55}

max=0
for i,j in per.items():
    if j>max:
        max=j
        no=i
            
print(f"{no} is ranker having {max} percentage...")