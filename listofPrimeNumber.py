'''
num = 11
# To take input from the user
# num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
'''

def check_prime(num):
    lower=2
    counter=0
    #print("Counter" + "--->" + "Prime Number")
    for num in range(lower, num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                counter+=1

                print(num)
    print("counter",counter)
check_prime(5100)
