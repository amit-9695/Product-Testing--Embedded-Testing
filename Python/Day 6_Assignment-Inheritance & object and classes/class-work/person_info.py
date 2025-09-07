class Person:
    def __init__(self,name,age,sex,weight,height):
        self.name=name
        self.age=age
        self.sex=sex
        self.weight=weight
        self.height=height
        
    def eating(self,msg):
        print(msg)
        
    def displayPersonInfo(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Sex: ",self.sex)
        print("Weight: ",self.weight)
        print("Height: ",self.height)

mark=Person("Mark",45,"Male",30,4.5)
mark.displayPersonInfo()
mark.eating("Can eat only Non-Veg Food")

print("------------------------------------")

sachin=Person("Sachin",55,"Male",70,5.5)
sachin.displayPersonInfo()
sachin.eating("Can eat only Veg Food")
