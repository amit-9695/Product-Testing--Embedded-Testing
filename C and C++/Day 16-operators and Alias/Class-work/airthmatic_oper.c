// Programs to perform arithmetic operations
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b, sum, difference, product, quotient;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    sum = a + b;
    difference = a - b;
    product = a * b;
    if (b != 0) {
        quotient = a / b;
        printf("Sum: %d\n", sum);
        printf("Difference: %d\n", difference);
        printf("Product: %d\n", product);
        printf("Quotient: %d\n", quotient);
    } else {
        printf("Sum: %d\n", sum);
        printf("Difference: %d\n", difference);
        printf("Product: %d\n", product);
        printf("Quotient: Division by zero error\n");
    }
    return 0;
}