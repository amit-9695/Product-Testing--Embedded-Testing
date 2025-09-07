// Program of assignement operators that modifies the value of a variable
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a = 10;
    int b = 5;
    printf("Initial values: a = %d\n", a);
    printf("Initial values: b = %d\n", b);
    a += 5;
    b -= 2;
    printf("Modified values: a = %d\n", a);
    printf("Modified values: b = %d\n", b);
    a *= 2;
    b /= 3;
    printf("After multiplication: a = %d\n", a);
    printf("After division: b = %d\n", b);
    a %= 3;
    printf("After modulus: a = %d\n", a);
    b <<= 1;
    printf("After left shift: b = %d\n", b);
    b >>= 1;
    printf("After right shift: b = %d\n", b);
    a &= 2;
    printf("After bitwise AND with 2: a = %d\n", a);
    return 0;
}