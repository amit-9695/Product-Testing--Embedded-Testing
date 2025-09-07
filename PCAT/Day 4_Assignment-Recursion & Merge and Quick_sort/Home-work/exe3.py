# Sum of first N natural numbers
def sum_nat(n):
    if n == 0:
        return 0
    return n + sum_nat(n - 1)

print(sum_nat(5))   # 15