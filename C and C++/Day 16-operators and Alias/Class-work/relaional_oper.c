// program to demonstrate the use of relational operators in C
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    if (a > b) {
        printf("%d is greater than %d\n", a, b);
    } else if (a < b) {
        printf("%d is less than %d\n", a, b);
    } else {
        printf("%d is equal to %d\n", a, b);
    }
    return 0;
}
