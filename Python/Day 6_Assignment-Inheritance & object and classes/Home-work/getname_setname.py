class Person:
    def __init__(self, name):
         self.name = name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
        
        
p=Person("john")
print(p.get_name())  
 
p.set_name("peter")
print(p.get_name())