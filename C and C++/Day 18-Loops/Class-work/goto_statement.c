// use goto jumping statement to create a vote elegibility checker
#include <stdio.h>
int main() {
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if (age < 0) {
        printf("Age cannot be negative. Please enter a valid age.\n");
        goto end;
    }

    if (age < 18) {
        printf("You are not eligible to vote.\n");
        goto end;
    }

    printf("You are eligible to vote.\n");

end:
    return 0;
}