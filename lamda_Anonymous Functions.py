from functools import reduce

f=lambda a:a*5

result=f(5)
print(result)

#let example
def iseven(n):
    return n%2==0

mylist=[1,2,3,4,5,6,7,8,9.10]
even=list(filter(iseven,mylist))
print(even)

even2=list(filter(lambda n:n%2==0,mylist))
print("my evern2: {}".format(even2))
#sum=sum(even2) +2
#sum 2 each entry
add2=list(map(lambda n:n+2,even2))
double=list(map(lambda n:n*2,even2))
#sum

sum=reduce(lambda a,b:a+b,even2)
print(add2)
print(double)
print(sum)