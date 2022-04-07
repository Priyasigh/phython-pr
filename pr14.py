'''
14. Write a python code to find out the names of students who have participated
 in all the games of inter college sports tournaments using python set.
'''
cricket={"manish","saurabh","henish","mann"}
chess={"akram","manni","saurabh","sunil"}
kabaddi={"mann","saurabh","sunil","karan"}

s1=cricket.intersection(chess)
result=s1.intersection(s1)
print("common students :",result)