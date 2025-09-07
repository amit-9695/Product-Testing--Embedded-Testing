str="Python is a dynamic programming language"
sub_str = "dynamic"

# To print the string
print(str)

#to convert the string to lower case
print(str.lower())

# to convert the string to upper case
print(str.upper())

# to chek the first occurence of the substring
print(str.find(sub_str))

# to chek the number of occurences of the substring
print(str.count(sub_str))

# replace the new strimg in which the substring is replaced
new_str = str.replace(sub_str, "static")
print(new_str)

# again replacing word 'static' with 'dynamic'
new_str = new_str.replace("static", sub_str)
print(new_str)

# replacing the word 'python' with 'java'
new_str = str.replace("Python", "Java")
print(new_str)


