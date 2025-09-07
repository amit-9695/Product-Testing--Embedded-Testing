// gets() used to read a line from stdin
#include <stdio.h>

int main() {
    char str[40];
    printf("Enter a string: ");
    gets(str); // Using gets to read a string
    printf("You entered: %s\n", str); // Print the string
    return 0;
}