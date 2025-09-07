# filter(fun,itrable) 
list1=[1,2,3,4,5,6]

#Using simple for loop to find the square of even numbers
sq_list=[]
for i in list1:
    if i % 2 == 0:
        sq_list.append(i )
        print([i])
print("<=======================================================>")

# Usinf filter, map, and reduce to find the square of even numbers
res=list(filter(lambda x: x % 2 == 0, list1))
print(res)
print("<=======================================================>")


# Finding the list those greater than 3 using filter method
greater_than_three = list(filter(lambda x: x > 3, list1))
print(greater_than_three)