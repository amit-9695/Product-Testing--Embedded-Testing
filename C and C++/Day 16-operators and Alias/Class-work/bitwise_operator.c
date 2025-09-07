// Program to demonstrate bitwise operators in C
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, and_result, or_result, xor_result, not_a, not_b;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    and_result = a & b;
    or_result = a | b;
    xor_result = a ^ b;
    not_a = ~a;
    not_b = ~b;
    printf("Bitwise AND: %d\n", and_result);
    printf("Bitwise OR: %d\n", or_result);
    printf("Bitwise XOR: %d\n", xor_result);
    printf("Bitwise NOT of first number: %d\n", not_a);
    printf("Bitwise NOT of second number: %d\n", not_b);
    return 0;
}
