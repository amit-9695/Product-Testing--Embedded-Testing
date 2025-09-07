// Program to swap two numbers without using a third variable
#include <stdio.h>
int main() {
    int a, b;
    printf("Enter First numbers: ");
    scanf("%d",&a);
    printf("Enter Second number: ");
    scanf("%d",&b);
    printf("Before swapping: a = %d, b = %d\n", a, b);
    a = a + b; 
    b = a - b; 
    a = a - b; 
    printf("After swapping: a = %d, b = %d\n", a, b);
    return 0;
}

