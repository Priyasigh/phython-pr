t=(2,3,45,60,77,98,9)
print("Even & odd tuple items=",t)

tE = tO =0

for i in t:
    if(i%2 == 0):
        tE = tE+1
    else:
        tO=tO+1

print("count of even numbers=",tE)
print("count of odd=",tO)