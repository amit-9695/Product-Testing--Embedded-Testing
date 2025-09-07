// ## symbol used to compine two tokens into one
#include <stdio.h>
#define CONCAT(a, b) a ## b

int main() {
    int var1 = 10, var2 = 20;
    printf("var1= %d\n", CONCAT(var, 1));
    printf("var2= %d\n", CONCAT(var, 2));
    return 0;
}