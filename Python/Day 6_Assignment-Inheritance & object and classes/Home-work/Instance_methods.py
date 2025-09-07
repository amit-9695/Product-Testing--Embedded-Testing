class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return (self.a + self.b)
    def sub(self):
        return (self.a - self.b)
    def mul(self):
        return (self.a * self.b)
    def div(self):
        return (self.a /self.b)
    
c1 = Calculator(10, 20)
print("Addition= ",c1.add())
print("Substraction= ",c1.sub())
print("Multiplication= ",c1.mul())
print("Division= ",c1.div())
