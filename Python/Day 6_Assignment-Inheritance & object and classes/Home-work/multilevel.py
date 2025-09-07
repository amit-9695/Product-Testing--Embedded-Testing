class C1:
    def __init__(self,a):
        print('C1 Constructor')
        self.var_a = a

class C2(C1):
    def __init__(self,a,b):
        super().__init__(a)
        print('C2 Constructor')
        self.var_b = b

class C3(C2):
    def __init__(self,a,b,c):
        super().__init__(a, b)
        print('C3 Constructor')
        self.var_c = c

obj = C3(10, 20, 30)
print('var_a =',obj.var_a)
print('var_b =',obj.var_b)
print('var_c =',obj.var_c)
