// Program o find the largest number among three numbers

#include <stdio.h>
int main() {
    int num1, num2, num3;
    printf("Enter First numbers: ");
    scanf("%d", &num1);
    printf("Enter Second number: ");
    scanf("%d", &num2);
    printf("Enter Third number: ");
    scanf("%d", &num3);
    if (num1 >= num2 && num1 >= num3) {
        printf("Largest number is: %d\n", num1);
    }   
    else if (num2 >= num1 && num2 >= num3) {
        printf("Largest number is: %d\n", num2);
    }
    else {
        printf("Largest number is: %d\n", num3);
    }
    return 0;
}