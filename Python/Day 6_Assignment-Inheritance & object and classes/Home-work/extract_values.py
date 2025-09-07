list=[10,20,'java','python',30.5,40.2,'php']
numericList=[]
stringList=[]
for item in list:
    if isinstance(item,(int,float)):
        numericList.append(item)
    elif isinstance(item,str):
        stringList.append(item)
print("String List :-", stringList)
print("Number List :-", numericList)
