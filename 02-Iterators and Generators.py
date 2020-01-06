'''
Problem 1

Create a generator that generates the squares of numbers up to some number N.
'''

def squaresnumber(n):
    for num in range(n):
        yield num**2


for x in squaresnumber(10):
    print(x)

    '''
    
Problem 2

Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:

    '''
import random
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)
for num in rand_num(1,10,12):
    print(num)

s = 'hello'

s = iter(s)

print(next(s))

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)