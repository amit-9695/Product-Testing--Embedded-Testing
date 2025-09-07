// program to find the maximum of three integers using nested if-else statements
#include <stdio.h>
#include <stdlib.h>
int main() {
    int num1;
    int num2;
    int num3;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    printf("Enter third number: ");
    scanf("%d", &num3);
    if (num1 >= num2) {
        if (num1 >= num3) {
            printf("Maximum number is: %d\n", num1);
        } else {
            printf("Maximum number is: %d\n", num3);
        }
    } else {
        if (num2 >= num3) {
            printf("Maximum number is: %d\n", num2);
        } else {
            printf("Maximum number is: %d\n", num3);
        }
    }
    return 0;
}