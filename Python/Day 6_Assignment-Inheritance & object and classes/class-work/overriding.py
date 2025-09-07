class Parent:
    def purchaseBike(self):
        print("Parent wants to purchase Hero Bike")
    def marry(self):
        print("Parent decided marry for our child with ABC")
    def property(self):
        print("Car+Gold+Money")

class Child(Parent):
    def purchaseBike(self):
        print("Child wants to purchase R1-5 Bike")
    def marry(self):
        print("Child decided marry with PQR")

c=Child()
c.property()
c.purchaseBike()


class Sim:
    def network(self):
        print("default network!!")
class Jio(Sim):
    def network(self):
        print("jio networl")

class BSNL(Sim):
    def network(self):
        print("BSNL network")

class Idea(Sim):
    def network(self):
        print("Idea network")

s1=Jio()
s1.network()
s2=BSNL()
s2.network()
s3=Idea()
s3.network()

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()
