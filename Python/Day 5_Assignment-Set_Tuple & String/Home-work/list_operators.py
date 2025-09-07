# The '+' operator
list1=[1,2,3]
list2=[4,5]

merge_list=list1+list2
print(merge_list)

print("-------------------")

# 'zip' function
for i,ele in zip(list1,list2):
    print(i,ele)
    
    
print("----------------------")

# The '*' operator
l1=[1,2,3]*2
l2=[4,5]*3
print("l1 = ",l1)
print("l2 = ",l2)

print("-------------------")


# Membership operator:-  'in' operator
name=["Amit","Atul","Suraj","Neeraj"]
print("Amit" in name)
print("Ankit" in name)