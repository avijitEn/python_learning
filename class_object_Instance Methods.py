class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        print ("{} is {} years old".format(self.name, self.age))

    # instance method
    def speak(self, sound):
        print("{} says {}".format(self.name, sound))

# Instantiate the Dog object
mikey = Dog("Mikey", 6)
mikey.description()
mikey.speak("yaho")