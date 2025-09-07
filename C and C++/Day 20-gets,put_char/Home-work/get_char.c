#include<stdio.h>
#include<ctype.h>

int main() {
    char ch;
    printf("Enter a character: ");
    scanf(" %c", &ch); // Note the space before %c to consume any leading whitespace
    if (isalpha(ch)) {
        printf("You entered an alphabetic character: %c\n", ch);
    } else if (isdigit(ch)) {
        printf("You entered a digit: %c\n", ch);
    } else {
        printf("You entered a special character: %c\n", ch);
    }
    return 0;
}