class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print("Hello my name is: " + self.name + ". I am " + str(self.age) + " yo.")

p1 = Person("János", 36)
p1.intro()

# __init__() == constructor in java
# __init__() is called every time the class is used
