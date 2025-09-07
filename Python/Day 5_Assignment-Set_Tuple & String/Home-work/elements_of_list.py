list1=[10,20,30,40,50,60,70,80,90]

#The other way of iterating a list based on the index value:

for i in range(0,len(list1)):
    print(f"{i}---> {list1[i]}")
    
print("-----------------------------")

# Iterating a list using "enumerate"
for (i,ele) in enumerate(list1):
    print(f"{i}---> {ele}")