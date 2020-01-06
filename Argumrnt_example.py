'''
pick even number , return even list

'''
def myfunc(*name):
    return (list(filter(lambda name:name%2==0,name)))
myfunc(7,8,9,10)