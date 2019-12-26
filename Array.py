#import array as arr
from array import *
val=array("i",[5,9,8,4,2])
#print(val)
#print(val.buffer_info())
#print(val.typecode)

for i in range(len(val)):
    print(val[i])

for b in val:
    print(b)
new=array(val.typecode,(a*a for a in val))
for i in new:
    print(i)