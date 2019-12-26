a=10
def something():
    #global a ## set global valriable , limitation not able to assign another local variable a
    x=globals()['a']
    a=15

    #you can assign global varibale
    globals()['a']=50
    print("global x",x)
    print("local a",a)

something()
print(a)