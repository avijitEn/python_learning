#Different method types in python

#In python there are three different method types. The static method, the class method and the instance method. Each one of them have different characteristics and should be used in different situations.

class Student:
        schoolname="kolkata"
        def __init__(self,m1,m2,m3):
            self.m1=m1
            self.m2=m2
            self.m3=m3

        def avg(self):    # this is instant Mehod
             return (self.m1+self.m2+self.m3)/3
        @classmethod       #class Method
        def schoolinfo(cls):
            print(f"my school name {cls.schoolname}")
        @staticmethod
        def schooltest():
            print("testt")

mysccholobject=Student(30,40,50)
mysccholobject2=Student(70,80,90)
print(mysccholobject.m1)
print(mysccholobject.m2)
print(mysccholobject.m1)
print(mysccholobject.avg())
print(mysccholobject2.avg())
mysccholobject2.schoolinfo()
mysccholobject2.schooltest()

