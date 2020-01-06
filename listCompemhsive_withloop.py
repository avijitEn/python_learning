mylist=[]
mystring="hello"
'''
for letter in mystring:
        mylist.append(letter)
print(mylist)
'''
'''
mylist=[letter for letter in mystring]
print(mylist)
'''
#one line for loop
#create
#mylist=[num for num in range(10)]
mylist=[num for num in range(11) if num%2==0]\

print(mylist)
mylist=[num**2 for num in range(1,11) if num%2==0]
print(mylist)
my-test=3

