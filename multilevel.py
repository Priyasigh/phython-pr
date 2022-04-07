class p1:
    def print1(self):
        print("first")

class p2:
    def print2(self):
        print("second")
    
class child(p1,p2):
    def print3(self):
        print("Child")

c=child()
# c.print1()
c.print2()
c.print3()
