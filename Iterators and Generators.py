# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for number in gencubes(10):
    print(number)

print("---------------------------------------------------")
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in genfibon(10):
    print(num)


def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b

    return output

print(fibon(10))