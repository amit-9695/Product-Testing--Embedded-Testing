// program to demonstrate pre-increment and post-increment operators in C
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a = 5;
    int b = 10;
    printf("Initial values: a = %d\t, ",a);
    printf("Initial values: b = %d\n", b);

    // Pre-increment
    printf("Pre-increment: a = %d\t,", ++a);
    printf("Pre-increment: b = %d\n", ++b);
    printf("Final values after pre-increment: a = %d, b = %d\n", a, b);

    // Post-increment
    printf("Post-increment: a = %d\t,", a++);
    printf("Post-increment: b = %d\n", b++);

    printf("Final values after post-increment: a = %d, b = %d\n", a, b);
    return 0;
}               