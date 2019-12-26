from numpy import *
arr=array([1,2,3,4])
arr=array([1,2,3,4],int)
print(arr)
##flot value supported numpy but not array
ar=array([1.2,1,4,5])
print(ar)
print(ar.dtype)

#line space
a=linspace(0,15,16) ##here 0 indicate --->start range , 15 indicate -->stop range 16 indicate -->part of range like 0 to 15 is 16 part
b=arange(1,15,2) #### arange is make steps here 2 indicate that ---steps like 1,3,5,7
c=logspace(1,40,5)  #it will indicate 10**1 to 10**40 and devide the 5 part
d=zeros(5)
e=ones(5)
f=ones(5,int)
print(a)
print(b)
print('%.2f' %c[0])
print('%.2f' %c[4])
print(d)
print(e)
print(f)