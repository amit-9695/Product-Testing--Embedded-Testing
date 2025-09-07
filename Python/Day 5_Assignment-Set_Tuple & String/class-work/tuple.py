t=(10,20,30,40,50)
print(type(t))
print(t)
print(t[0])
for ele in t:
    print(ele)
    
# we can also declear tupple like yhis
t2=10,20,30
print(t2)

# unpacking the tupple element 
a,b,c=t2
print(f"a:{a} , b:{b} , c:{c}")

# merge two tupple 
t3=10,20,30
t4=40,50
print(t3+t4)

# merge two tupple using "zip" function
c=zip(t3,t4)
print(type(c))

for a,b in zip(t3,t4):
    print(a,b)