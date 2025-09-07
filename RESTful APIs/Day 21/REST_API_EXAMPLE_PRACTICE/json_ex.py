import json
json_str= '{"name": "John", "age": 30, "city": "New York"}'

print("JSON String:", json_str)

data=json.loads(json_str)
print("Parsed JSON Data:", data)
print("Name:", data['name'])
print("Age:", data['age'])
print("City:", data['city'])
print("<======================================================>")

# Creating jason using List and Dictionary

jason_str_obj="""[
    {
        "name": "Alice",    
        "age": 25,
        "city": "Los Angeles"
        },
    {
        "name": "Bob",
        "age": 28,
        "city": "Chicago"
    },
    {
        "name": "Charlie",
        "age": 22,
        "city": "Miami"
    }
]

"""

data=json.loads((jason_str_obj))