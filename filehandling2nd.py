"""
with open("myfile.txt") as f:
    for line in f:
        print(line.strip())
        d=open("test2","a")
        e=line.strip()
        d.write(line.strip())
        """
"""
    x=open("myfile.txt")
    y=open("mytest2.txt","a")
    z=x.read()
    y.write(z.strip())
    y.close()
    x.close()

"""
'''
import keyword
print(keyword.kwlist)
for element in keyword.kwlist:
        print(element)
'''

mylist=[7,3,4,1]
d=0
for num in range(len(mylist)):
    d+=mylist[num]
    #print(mylist[num])
print(d)
print(enumerate(mylist))

#print(s)