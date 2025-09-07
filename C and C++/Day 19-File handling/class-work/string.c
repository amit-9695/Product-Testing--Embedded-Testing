# include<stdio.h>
#include<string.h>

void main(){
    char name[]="John Doe";
    int len1,len2;
    len1 = strlen(name);
    len2=strlen("Amit Shukla");
    printf("Length of name: %d\n", len1);
    printf("Length of 'Amit Shukla': %d\n", len2);
}