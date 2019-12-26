from numpy import *
arr=array([
    [1,2,3,4],
    [3,4,6,7]

]

)
print(arr)
print(arr.ndim) #dimensean
print(arr.shape)
print(arr.size)
#convert 2 to 1
arr2=arr.flatten()
print(arr2)