class Computer:
    def __init__(self):
        self.name="avijit"
        self.age=34



l2=Computer()
l3=Computer()
print(l2.name)
print(l3.name)
print(id(l2))
print(id(l3))
l2.name="test"
l2.age=22
print("name {} and age {}".format(l2.name,l2.age))