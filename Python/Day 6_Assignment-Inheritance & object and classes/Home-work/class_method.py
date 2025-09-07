class Car:
    wheels=4
    @classmethod
    def run(cls,name):
        print('{} runs with {} wheels...'.format(name,cls.wheels))
Car.run('Maruti')
Car.run('Ford')