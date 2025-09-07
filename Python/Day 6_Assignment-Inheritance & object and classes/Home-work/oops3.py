class Demo:
    def __init__(self):
        self.a=10
        self.b=20
        
    def f1(self):
        self.c=30
        
    def f2(self):
        self.d=40
        
d1=Demo()
print(d1.__dict__)

#Creating instance variable
d1.f1()
# here you can see after creating instance variable one more value added - c:30
# __dict__ method display the object in dictionary format
print(d1.__dict__)

d1.f2()
print(d1.__dict__)