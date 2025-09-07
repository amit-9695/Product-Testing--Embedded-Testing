# Valur condition logic in dictionary comprehension
# create a dictionary in range (1to 10)and value return even if key is even otherwise odd
dic = {num:"even" if num%2==0 else "odd" for num in range(1,11 )}
print(dic)