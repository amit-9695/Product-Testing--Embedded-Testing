#include<stdio.h>
#include<string.h>

void main() {
    char str1[]="Hello world!";
    char str2[10];

    strcpy(str2, str1);
    printf("String 1: %s\n", str1);
    printf("String 2 (after copy): %s\n", str2);

    strcpy(str2,str1+1);
    printf("String 2 (after modification): %s\n", str2);
}
