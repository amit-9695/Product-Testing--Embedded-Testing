class Bank:
    pass

#Creating subclass
class SBI(Bank):
    pass

#Creating sub class of SBI 
class HDFC (SBI):
    pass


print(issubclass(SBI,Bank))

print(issubclass(Bank, SBI)) 

print(issubclass(HDFC, Bank))

print(issubclass(HDFC,HDFC))

print(issubclass(Bank, object))
