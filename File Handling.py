
file=open("myfile.txt","w")
file.write("""ttttttttttttttt
2nd line 
34d 

last line
""")
file.close()
data=open("myfile.txt","r")
data.close()
#print(str(data.read().split()))
#for each in data:
    #print (each.strip().strip())
#print ("".join([s for s in data.strip().splitlines(True) if s.strip("\r\n").strip()]))

with open("myfile.txt","r") as data:
    f=data.read()
    #print(f.strip())

#now remove the space line
data=open("myfile.txt","r")

"""list=[]
counter=0
for line in data:
    counter += 1
    if not line.isspace():
        list.append(line)
        temp=line.strip()
        print(temp,counter)
    #print(f"{counter}  {line}")
"""
#Appand the file
f=open("myfile.txt","a")
f.write("tttttttttttttttttttttt\nbbbbbbbbbbbbbbbbbbbbbb\nnnnnnnnnnnnnnnnnnnnnnnnn")
f.close()

myread=open("myfile.txt","r")
print(myread.read())





