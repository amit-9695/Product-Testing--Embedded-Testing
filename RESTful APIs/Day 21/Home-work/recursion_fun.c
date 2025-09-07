// Factorial number using  tail recursion

#include <stdio.h>

int factorial(int n){
    if (n<0){
        return -1;
    }
    if (n==0){
        return 1;
    } else {
        return (n * factorial(n - 1));
    }
}

void main() {
    int fact =0;
    fact=factorial(5);
    printf("Factorial of 5 is %d\n", fact);
}