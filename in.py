class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print (self.firstname,self.lastname)

p= person("jay","patel")
p.printname()

class student(person):
    def __init__(self, fname, lname):
        self.firstname=lname
        self.lastname=fname

s=student("smit","patel")
s.printname()