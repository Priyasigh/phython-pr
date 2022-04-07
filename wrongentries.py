tp=(10,20,250,-10)

def marks(tp):
    ls=[]
    for i in tp:
        if i >0 and i < 100:
            ls.append(i)
        else:
            print(f"{i} is incorrect marks")
        m=tuple(ls)
    return m

print(marks(tp))