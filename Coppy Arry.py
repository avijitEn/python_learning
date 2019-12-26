from numpy import *
arr1=array([1,2,3,4])
arr2=arr1 # simpley we can do assign new allise but same memory address
print(id(arr1))
print(id(arr2))
#let chnage the array view
arr2=arr1.view()
print(id(arr1))
print(id(arr2)) # now you can chnage the memory location
#shaellw copy
#now if we chnage the any of arry , it will reflect both arrow

arr1[1]=5
print(arr1)
print(arr2)

arr2=arr1.copy()
print(arr2)