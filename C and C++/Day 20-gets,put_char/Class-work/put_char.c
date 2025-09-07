#include<stdio.h>
#include<ctype.h>

int main(){
    char ch;
    printf("Enter a character: ");
    ch = getchar(); // Using getchar to read a single character

    if (islower(ch)) {
        putchar(toupper(ch)); // Convert to uppercase if it's lowercase
    } else if (isupper(ch)) {
        putchar(tolower(ch)); // Convert to lowercase if it's uppercase
    } else {
        putchar(ch); // Print the character as is if it's neither
    }
    return 0;
}