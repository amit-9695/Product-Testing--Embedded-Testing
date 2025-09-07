// A macro in C is a preprocessor directive that defines a piece of code to be replaced before compilation. Macros are defined using #define. 

#include <stdio.h>
#define PI 3.14159        // Define a macro for the value of PI
 
int main() {
    float r = 2;
    float area = PI * r * r;
    printf("Area of circle with radius %.2f is %.2f\n", r, area);
    return 0;
}