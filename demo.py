'''num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))
num4 = float(input('Enter four number: '))
num5 = float(input('Enter fifth number: '))

sum=num1+num2+num3+num4+num5

print('sum = ',sum)
'''
'''sum=0

for i in range(1,6):
  n=input("enter number")
  sum=sum+int(n)

print("sum=",sum)
'''

max=0

for i in range(1,6):
    n=input("enter number")

    if(int(n)>max):
        max=int(n)

print("max=",max)