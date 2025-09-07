# split '/' symbol in a date string
date_string = "2023/10/23"
print("Original date string:", date_string)
print("After splitting the date string:", date_string.split('/'))
# Splitting the date string into components
date_components = date_string.split('/')
print("Year:", date_components[0])
print("Month:", date_components[1])
print("Day:", date_components[2])