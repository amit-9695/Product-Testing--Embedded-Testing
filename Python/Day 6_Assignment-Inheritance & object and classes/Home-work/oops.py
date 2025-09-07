class person:
    def __init__(self):
        print("person object created")
        self.name="Amit"
        self.age=20

# Creating object of a person class
# when we create an object one memory ia allocated
obj1=person()
print("Name: ",obj1.name)

obj2=person()
print("Name: ",obj2.name)