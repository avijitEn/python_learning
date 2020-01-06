
'''

Capitalise every other letter in a string
'''

def myfunc(name):
    #even idex check
    r=""
    b=True
    for c in name:
        r += c.upper() if b else c.lower()
        #print(c)

        if c.isalpha():
            b = not b
    print( r)


myfunc ("avijit")

