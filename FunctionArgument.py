'''def Persion(name,age):
   print(name)
   print(age)

Persion("avijit",32) # position dependent
Persion(name="newxustomer",age=28) #key ward base'''
#lengh not sure that case

def sum(x,*y):
    z=x
    for i in y:
       z=z+i
    print(z)
sum(1,2,3,4,5)