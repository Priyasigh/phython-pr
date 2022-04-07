
'''
def check_prime(n):
    i = 2
    p = 1

    while i < n:
        if n % i == 0:
            p = 0
            break
        i = i + 1

    return p


x = int(input("Enter a number:"))
p = check_prime(x)

if p == 1:
    print("Number is prime:", x)
else:
    print("Number is not prime:", x)

    '''

n=input("enter the number")
no=int(n)


def prime(no):
  for i in range(2,no):
      if no%i==0:
          return 0
  else:
      return 1

ans=prime(no)
if ans == 1:
    print("Number is prime:")
else:
    print("Number is not prime:")
 

