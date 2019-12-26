from array import *
#create empty array
arr=array("i",[])
#ask for lenght of array
lenghthofarry=int(input("enter the lenght"))
for i in range(lenghthofarry):
    #apapend the array with user input value
    arr.append(int(input("pleaseenter next")))
print(arr)

#let serch the array valuw
find=int(input("please enter the serch value: "))
#1st Method to serch
print(arr.index(find))
###2nd steps below 
k=0 ### assign the index value

for e in arr:
    if e==find:
            print("find the match index ", k)
            break

    k+=1
else:
    print("not found the serch value")