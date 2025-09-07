""" Program 2:-
Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
The flowers are identified using name, price per kg and stock available (in kgs).
Write a Python program to implement the above requirement.
Details of Flower class are given below:
Class name: Flower
  

 
Flower Name	Level(in Kgs)
Orchid	15
Rose	25
Jasmine	40
Note: Perform case insensitive string comparison
Represent few flowers, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""
class Flower:
    def __init__(self, name, price_per_kg, stock):
        self.name = name
        self.price_per_kg = price_per_kg
        self.stock = stock

    def set_name(self, name):
        self.name = name

    def set_price_per_kg(self, price):
        self.price_per_kg = price

    def set_stock(self, stock):
        self.stock = stock

    def is_below_level(self):
        levels = {
            "orchid": 15,
            "rose": 25,
            "jasmine": 40
        }
        return self.stock < levels.get(self.name.lower(), float('inf'))

    def __str__(self):
        return f"Flower Name: {self.name}, Price per kg: {self.price_per_kg}, Stock: {self.stock} kg"
    
# Example usage
if __name__ == "__main__":
    flower1 = Flower("Orchid", 100, 10)
    flower2 = Flower("Rose", 50, 30)
    flower3 = Flower("Jasmine", 80, 35)

    for flower in [flower1, flower2, flower3]:
        print(flower)
        if flower.is_below_level():
            print("Alert: Stock is below the required level!")
        else:
            print("Stock is sufficient.")