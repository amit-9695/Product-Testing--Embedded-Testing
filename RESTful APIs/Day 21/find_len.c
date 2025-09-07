// To find the length of a string using the strlen function in C

# include<stdio.h>
#include<string.h>

int main(){
    char str[] = "Hello, World!";
    int len = strlen(str);  // Use the strlen function to find the length of the string
    printf("Length of the string is: %d\n", len);
    return 0;
}