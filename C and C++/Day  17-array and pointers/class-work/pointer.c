# include <stdio.h>
void main() {
    int num1=5;
    int *ptr1;
    ptr1 = &num1;
    int **ptr2;
    ptr2=&ptr1;
    printf("Value of num1: %d\n", num1);
    printf("Address of num1: %p\n", &num1);
    printf("Value of ptr1: %d\n", *ptr1);
    printf("Address of ptr1: %p\n", &ptr1);
    printf("Value of ptr2: %d\n", **ptr2);
    printf("Address of ptr2: %p\n", &ptr2);
}