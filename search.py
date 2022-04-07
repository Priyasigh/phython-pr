import numpy as np 
arr=np.array([3,5,7,1,6])

no=int(input("Enter number to search : "))
pos=0
for i in arr:
    if no==i:
        print(f"Element is exist in {pos} position ")
        break
    else:
        pos=pos+1
else:
    print("Element is not present in the array")