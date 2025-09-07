class NotEligibleException(Exception):
    pass
class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def check_salary(self):
        if(self.__salary < 2000):
            raise NotEligibleException
            return False
        else:
            return True

emp1=Employee(5000)
emp2=Employee(1000)
try:
    status=emp1.check_salary()
    print(status)
    status=emp2.check_salary()
    print(status)
except NotEligibleException:
    print("Not Eligible")
