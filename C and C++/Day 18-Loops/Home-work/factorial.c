// Program to print the factorial of a number

#include <stdio.h>
int main() {
    int n;
    int factorial = 1;

    printf("Enter a natural number: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Please enter a natural number greater than or equal to 0.\n");
        return 1;
    }

    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }

    printf("The factorial of %d is: %d\n", n, factorial);
    return 0;
}