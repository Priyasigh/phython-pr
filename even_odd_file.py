import even_odd
fpeven=open("Even.txt","a")
fpodd=open("Odd.txt","a")
for i in range(1,5):
    no=input("Enter Number")
    ret=even_odd.even_odd(no)
    if ret==0:
        fpeven.write(no+'\n')
    else:
        fpodd.write(no+'\n')