class User:
    def __init__(self,name,age,mno):
        self.name=name
        self.age=age
        self.mno=mno
class Employee(User):
    def __init__(self,name,age,mno,specialization):
        super().__init__(name,age,mno)
        self.specialization=specialization

class Manager(User):
    def __init__(self,name,age,mno,department):
        super().__init__(name,age,mno)
        self.department=department


#Create a Employee Object
e1=Employee('John',30,9897675432,'Python Prog')
print('......Employee Details......')
print('Name = ',e1.name)
print('Age = ',e1.age)
print('Mno = ',e1.mno)
print('Specialization = ',e1.specialization)
print('--------------------------------------')
m1=Manager('Harry',45,8989767645,'Sales')
print('......Manager Details......')
print('Name = ',m1.name)
print('Age = ',m1.age)
print('Mno = ',m1.mno)
print('Department =',m1.department)
