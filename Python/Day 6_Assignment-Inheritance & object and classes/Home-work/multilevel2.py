class GrandParent:
    def __init__(self):
        print('Grandparent Constructor!.')
    def displayGrandParent(self):
        print('Grandparent Method!.')

class Parent(GrandParent):
    def __init__(self):
        print('Parent Constructor!.')
    def displayParent(self):
        print('parent Method!.')

class Child(Parent):
    def __init__(self):
        print('Child Constructor!.')
    def displayChild(self):
        print('Child Method!.')

#Create Child class Object
obj=Child()
obj.displayGrandParent()
obj.displayParent()
obj.displayChild()
