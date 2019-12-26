def persion(name,**data): #you have to pass ** while pass keyword argument in function calling
    print(name)
    print(data)
    for i,j in data.items():
        print(i,'|',j)

#persion("avijit",29,"citynane",8888888)
persion("avijit",age=29,cityname="citynane",mobile=8888888)