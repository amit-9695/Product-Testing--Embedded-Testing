// Program to demonstrate ternary operators in C
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, max;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    // Using ternary operator to find the maximum of two numbers
    max = (a > b) ? a : b;
    printf("Maximum number is: %d\n", max);
    return 0;
}
