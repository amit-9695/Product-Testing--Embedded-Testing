class Demo:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
        self.e=50
    def removeA(self):
        del self.a       # delete instance variable With-in class
        
# instantiate the Demo class
d1=Demo()
print(d1.__dict__)
print("=============================================>")

d1.removeA()
print(d1.__dict__)
print("================================>")

# delete instance variable outside of class
del d1.c
print(d1.__dict__)
print("<=============================================================================>")


#The instance variables which are deleted from one object, will not be deleted from other objects because for each object a separate copy will be maintained.
d2=Demo()
print(d2.__dict__)
