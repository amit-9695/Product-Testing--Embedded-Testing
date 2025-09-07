// To take input as a string we dont use '&' in scanf
// because the name of the array itself acts as a pointer to the first element.

# include<stdio.h>
int main(){
    char name[10];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello, %s!\n", name);
    return 0;
}