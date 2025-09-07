//  Printting sum of n natural numbers

#include <stdio.h>

int main() {
    int n, sum = 0;

    printf("Enter a natural number: ");
    scanf("%d", &n);

    if (n < 1) {
        printf("Please enter a natural number greater than 0.\n");
        return 1;
    }

    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    printf("The sum of the first %d natural numbers is: %d\n", n, sum);
    return 0;
}