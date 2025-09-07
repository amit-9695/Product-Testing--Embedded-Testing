class C1:
    def __init__(self):
        print('C1-Class Constructor!')

class C2(C1):
    def __init__(self):
        super().__init__()
        print('C2-class Construtor!.')

#creating child class object
obj=C2()
