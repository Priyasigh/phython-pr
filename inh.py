class person:
    def __init__(self,fname,lname):
        self.firstname=lname
        self.lastname=fname

    def printname(self):
        print (self.firstname,self.lastname)

class student(person):

    def __init__(self, fname, lname,eno):
        person. __init__(self,fname,lname)
        self.firstname1=fname
        self.lastname2=lname
        self.enrollmentno=eno
    def stud(self):
        print(self.firstname1,self.lastname2,self.enrollmentno)

s=student("smit","patel",1001)
s.printname()   
s.stud()        