"""  is an equation with degree 2 in the form of ax2 +bx + c = 0 where a, b and c are the coefficients.
ImplementQuadratic equation a program to solve a quadratic equation.
Find the discriminant value using the formula given below.
discriminant = b2 - 4ac
If the discriminant is 0, the values of both the roots will be same. Display the value of the root.
If the discriminant is greater than 0, the roots will be unequal real roots. Display the values of both the roots.
If the discriminant is less than 0, there will be no real roots. Display the message "The equation has no real root"
Use the formula given below to find the roots of a quadratic equation.
x = (-b ± discriminant)/2a
 """

a=int(input("Enter the coefficient a: "))
b=int(input("Enter the coefficient b: "))
c=int(input("Enter the coefficient c: "))

def solve_quadratic(a, b, c):
    discriminant = (b**2) - (4*a*c)
    if discriminant == 0:
        root_positive = (-b +discriminant)/ (2 * a)
        root_negative = (-b - discriminant) / (2 * a)
        return f"The root is: {root_positive} and {root_negative} "
    elif discriminant > 0:
        root_positive = (-b + discriminant) / (2 * a)
        root_negative = (-b - discriminant) / (2 * a)
        return f"The roots are: {root_positive} and {root_negative}"
    else:
        return "The equation has no real root"
    
result = solve_quadratic(a, b, c)
print(result)
    