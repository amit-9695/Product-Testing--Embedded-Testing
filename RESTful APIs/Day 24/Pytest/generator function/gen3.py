# generate first n numbers

def generate_numbers(num):
    print("Generating numbers up to", num)
    n=1
    while n <= num:
        yield n
        n += 1
        
values = generate_numbers(5)

for x in values:
    print(x)