// Program that demonstrates the use of unary operators in C
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Enter another number: ");
    scanf("%d", &b);
    printf("Original a: %d, b: %d\n", a, b);
    a++;
    b--;
    printf("Updated a: %d, b: %d\n", a, b);
    return 0;
}