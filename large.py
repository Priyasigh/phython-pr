# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
#num1 = -1
#num2 = -5
#num3 = -12

# uncomment following lines to take three numbers from user
#for i in range(1,6):
 #   n=input("enter number")
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
'''

lst = []
#num =input('How many numbers: ')
for n in range(1,6):
    numbers = input('Enter number ')
    lst.append(numbers)
print("Maximum element in the list is :", max(lst))