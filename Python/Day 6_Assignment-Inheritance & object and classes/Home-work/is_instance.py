class Test1:
    pass

class Test2(Test1):
    pass

t1=Test1()
t2=Test2()
 
print('t1 is the Instance  of Test1 - ',isinstance(t1,Test1))
print('t1 is the Instance of Test2 - ',isinstance(t1,Test2))
print('t2 is the Instance  of Test2 - ',isinstance(t2,Test2))
print('t2 is the Instance of Test1 - ',isinstance(t2,Test1))
