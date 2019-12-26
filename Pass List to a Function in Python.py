def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
mylist=[1,2,3,4,5,6,7,8,9,10]
even,odd=count(mylist)
print("even: {} and Odd: {}".format(even,odd))