import numpy as np
a=np.array([-200,-10,-30,-40,-66])
print(a)

max=a[0]
min=a[0]
for i in a:
    if i>max:
        max=i
        
        
for i in a:
    if i<min:
        min=i
   
print("max",max)
print("min",min)