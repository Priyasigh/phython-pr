class c1:
    def __init__(self):
        self.name1="python"
        print("first")

class c2:
    def __init__(self):
        self.name2="programming"
        print("second")

class child (c1,c2):
    def __init__(self):
        c1. __init__(self)
        c2. __init__(self)
        print("child")
    
    def printname(self):
        print(self.name1,self.name2)
        
obj=child()
obj.printname()
