num=7
for i in range(2,num):
    if num%i==0:
        print("Not a prime")
        break
else:
    print("Number is a prime")