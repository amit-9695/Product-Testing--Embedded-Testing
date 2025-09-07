class NotEligibleException(Exception):
    pass
class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def check_salary(self):
        try:
            if(self.__salary < 2000):
                raise NotEligibleException
            else:
                return True
        except NotEligibleException:
            print("1")
            raise NotEligibleException

emp1=Employee(1000)
try:
    status=emp1.check_salary()
    print("2")
except NotEligibleException:
    print("3")
