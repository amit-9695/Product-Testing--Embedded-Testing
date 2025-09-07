// Finding the Quotient and Remainder
#include <stdio.h>
int main() {
    int dividend, divisor, quotient, remainder;
    printf("Enter dividend: ");
    scanf("%d", &dividend);
    printf("Enter divisor: ");
    scanf("%d", &divisor);
    if (divisor != 0) {
        quotient = dividend / divisor;
        remainder = dividend % divisor;
        printf("Quotient = %d\n", quotient);
        printf("Remainder = %d\n", remainder);
    }
    else {
        printf("Error: Division by zero is not allowed.\n");
    }
    return 0;
}
