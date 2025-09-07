list1=[1,2,3,4,5,6,7,8]
list2=[6,7,8,9,10]
# Finding list of common elements in two lists using list comprehension
common_elements=[x for x in list1 if x in list2]
print(common_elements)
