def number(n):
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

res=number(12345)
print(res)  # Output: 5