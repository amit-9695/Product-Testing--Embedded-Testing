class person:
    def __init__(self,name,age):
        print("person object created")
        self.name=name
        self.age=age

# Creating object of a person class
# when we create an object one memory ia allocated
obj1=person("Amit",21)
print("Name: ",obj1.name)

obj2=person("Atul",21)
print("Name: ",obj2.name)