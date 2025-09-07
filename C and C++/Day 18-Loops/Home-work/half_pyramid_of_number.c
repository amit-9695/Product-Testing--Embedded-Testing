// Create a half pyramid of numbers in C

#include <stdio.h>

int main() {
    int n;

    printf("Enter the number of rows for the half pyramid: ");
    scanf("%d", &n);

    if (n < 1) {
        printf("Please enter a natural number greater than 0.\n");
        return 1;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }

    return 0;
}