class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
    
    
#create an Object
p1=Person()
p1.setName('john')
p1.setAge(101)
print("Name= ",p1.getName())
print("Age= ",p1.getAge())
