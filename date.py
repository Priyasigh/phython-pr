import datetime
td=datetime.date.today()
class stud:
    def __init__(self,name,day,month,year):
        self.studname=name
        self.bday=day
        self.bmonth=month
        self.byear=year

    def pri(self):
        c_year=td.year
        c_month=td.month
        c_day=td.day

        age_y=(c_year-self.byear)-1
        age_m=abs(c_month-self.bmonth)
        age_d=abs(c_day-self.bday)
        print(f"{self.studname} you are {age_d} days {age_m} months and {age_y} years old")

s=stud("ankita",15,10,2000),("priya",11,12,1998)
# s1=stud("priya",11,12,1998)
s2=stud("nency",14,3,2001)
s.pri()
# s1.pri()
s2.pri()