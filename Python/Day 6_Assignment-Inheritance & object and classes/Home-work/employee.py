class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id)
        print(self.name)

e=Employee(101,'Scott')
e.display()
