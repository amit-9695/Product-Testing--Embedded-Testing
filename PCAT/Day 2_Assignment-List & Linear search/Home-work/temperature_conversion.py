# Converting c to f
# Formula: F = C * 9/5 + 32

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")