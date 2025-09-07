//  program to compare two integers, and chek if the first number completely divides the second number using modulus operator
#include <stdio.h>
#include <stdlib.h>
int main() {
    int num1, num2;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    if (num1 > num2) {
        printf("%d is greater than %d\n", num1, num2);
    }
    else if (num1 < num2) {
        printf("%d is less than %d\n", num1, num2);
    }
    else {
        printf("%d is equal to %d\n", num1, num2);
    }

    
    if (num2 != 0) {
        if (num1 % num2 == 0) {
            printf("%d completely divides %d\n", num1, num2);
        } else {
            printf("%d does not completely divide %d\n", num1, num2);
        }
    } else {
        printf("Division by zero error\n");
    }
    return 0;
}
