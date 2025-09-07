class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying a phone")
            
        
        
class FeaturePhone(Phone):
    pass
fp=FeaturePhone(10000,"Apple","50 MP")
print("price : ",fp.price)
print("Brand : ",fp.brand)
print("Camera : ",fp.camera)


        