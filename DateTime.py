import datetime
t=datetime.time(5,2,1)
print(t)
print(t.hour)
print(datetime.time.min)
print(datetime.time.max)

today=datetime.date.today()
print(today.timetuple())