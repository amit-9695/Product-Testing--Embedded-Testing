class C1:
    def __init__(self,a):
        print('C1-Class Constructor!')
        self.a=a

class C2(C1):
    def __init__(self,a,b):
        super().__init__(a)
        print('C2-class Construtor!.')
        self.b=b
    def display(self):
        print('a = ',self.a,'b= ',self.b)

obj=C2(10,20)
obj.display()
