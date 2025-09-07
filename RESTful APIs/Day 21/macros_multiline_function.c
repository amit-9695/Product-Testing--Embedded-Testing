// defining a multiline macro to print values
# include<stdio.h>
#define PRINT_VALUE(x,y) \
    printf("The value is: %d\n", (x)); \
    printf("The value is: %d\n", (y));

int main() {
    int a = 10, b = 20;
    PRINT_VALUE(a, b);  // Use the macro to print values of a and b
    return 0;
}
    