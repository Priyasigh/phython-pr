
name=input("enter name")

def count_vowel(name):
    vowels=0

    for i in name:
        if (i =='a' or i=='e' or i=='i' or i=='o' or i=='u'):    
            vowels=vowels+1
    return vowels
vwl=count_vowel(name)
print("No of vowels:->",vwl)
'''
name=input("Enter the name : ")

def vowel(name):
    vowel=0
    for i in name:
        if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowel+=1
    return vowel

output=vowel(name)
print("number of vowel :" ,output)
'''