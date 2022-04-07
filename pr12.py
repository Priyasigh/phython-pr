'''
12. write a python function to find incorrect marks entries (marks<100 or marks>0)
 from the given tuple and delete such entries from the tuple.
'''
marks=(10,20,250,2000,-25,86,-90)

def valid_marks(marks):
    ls=[]
    for i in marks:
        if i > 0 and i <=100:
            ls.append(i)
        else:
            print(f"{i} is incorrect mark...")    
       
        m=tuple(ls)
    return m

print(valid_marks(marks))