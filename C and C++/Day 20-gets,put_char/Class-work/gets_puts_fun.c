// gets() used to read a line from stdin
#include <stdio.h>

int main() {
    char str[40];
    puts("Enter a string: ");
    gets(str); // Using gets to read a string
    puts("String Name: ");
    puts(str); // Print the string
    printf("You entered: %s\n", str); // Print the string
    return 0;
}