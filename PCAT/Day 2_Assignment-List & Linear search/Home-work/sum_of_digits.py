# Finding the sum of the gven digits

num=int(input("Enter any Number"))

def sum_of_digits(num):
    sum= 0
    while num>=0:
        d= num % 10
        num= num // 10
        sum= sum + d
    return sum

result = sum_of_digits(num)
print(f"The sum of the digits is: {result}")