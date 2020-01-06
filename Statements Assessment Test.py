'''
#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
d=st.split()
for i in d:
    if i[0]=='s':
        print( "match the word:",i)
'''
#Use range() to print all the even numbers from 0 to 10.
'''
for i in range(11):
    if i%2==0:
        print(i)
        
        '''


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
'''
for i in range(1,50):
    if i%3==0:
        print(i)
   '''
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
if len(st)%2==0:
    print("even")


    #Write a function that checks whether a number is in a given range (inclusive of high and low)
    def Check_range(num,low,high):
        if num in range(low,high):
            print('{} is in the range between {} and {}'.format(num, low, high))
        else:
            print('The number is outside the range.')

Check_range(10,2,9)



