def triple(x):
    return x * 3

def square(x):
    return x ** 2

def first_char(s):
    return s[0]

triple_list=list(map(triple, range(11)))  
squre_list=list(map(square, range(11)))
first_char_list=list(map(first_char, ['apple', 'banana', 'cherry'])) 
print("Triple List:", triple_list)
print("Square List:", squre_list)
print("First Character List:", first_char_list) 