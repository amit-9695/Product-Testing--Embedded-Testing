# using condition in dictionary comprehension
# create a dictionry where keys are from 1 to 10 but add a conditon that the keys are only even number and the vaue is squre of key
even_squre={num:num **2 for num in range(1, 11) if num%2==0}
print(even_squre)