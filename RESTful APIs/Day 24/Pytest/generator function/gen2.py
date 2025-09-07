def count_down(n):
    print("Starting countdown from", n)
    while n > 0:
        yield n
        n -= 1
        
values = count_down(5)

for x in values:
    print(x)