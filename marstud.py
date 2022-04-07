'''

import numpy as np

arr=np.array([[24,43,50],[30,25,34],[12,45,34]])

sum=0 
for i in arr:
    sum=0
    for j in i:
        sum=sum+j      
    print(sum)
'''
import numpy as np
a=np.array([[60,70,80],[40,50,60],[45,55,65]])

max=0  
for i in a:
    total=0
    for j in i:
        total=total+j        
    print("total is : " ,total)
    
#     per=total/3
#     print("per:",per)
   
#     if per>max:
#         max=per
        
# print(f"With {max} percentage you are Ranker....")