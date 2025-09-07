class Car:
    #class Attribute
    Type1= "Four wheeler" 
    def read(self):
        self.name="Maruti" 
    def show(self):
        print(self.name)
        print(Car.Type1) 
class Bike(Car):
    #class attribute
    Type2 = "Two wheeler" 
    def read1(self):
        self.name="HONDA" 
    def show1(self):
        print(self.name)
        print(__class__.Type2) 
#Crating a Base class Object
print('With Respect to Base Object')
c=Car()
c.read()
c.show()
#Crating a Derived class Object
print('With Respect to Derived Object')
bike=Bike()
bike.read()
bike.show()
bike.read1()
bike.show1()
