#simple function

from os import name


def print_name():
    print("hello")

print_name()

#function with argument

def print_name(name):
    print(name)

print_name("priya")

#multiple arguments

def sum(a,b):
    sum=a+b
    print("sum=",sum)

sum(100,200)

#return statement

def sum(a,b):
    sum=a+b
    return sum

ans=int(sum(1000,2000))
print("sum=",ans)

#default arguments

def test(name="priya"):
    print(name)

test("ankita")
test()

#arbitary arguments

def test(*a):
    print(a[0],a[2])

test("mehsana","kherva","baroda")

#keyword arguments

def stud_detail(eno,ename,city):
    print("Eno=",eno,"Ename=",ename,"City=",city)

stud_detail(city = "Gandhinagar",eno="1001",ename="priya")


#arbitary keyword arguments

def stud_detail(**stud):
    print(stud["eno"],stud["name"],stud["city"])

stud_detail(eno=101,name="priya",city="baroda")