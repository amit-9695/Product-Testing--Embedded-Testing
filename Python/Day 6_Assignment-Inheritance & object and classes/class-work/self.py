class Product:
    productId=100
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand
        Product.productId +=1
    def displayPrdouctDetails(self):
        print("ProductId:",Product.productId)
        print("ProductName:",self.name)
        print("ProductPrice:",self.price)
        print("ProductBrand:",self.brand)
        
        
prod1=Product('Ipad',10000,'Apple')
prod1.displayPrdouctDetails()
print("============================")
prod2=Product('Redmi4A',10000,'Redmi')
prod2.displayPrdouctDetails()
