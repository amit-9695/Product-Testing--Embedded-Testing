# include<stdio.h>

void main(){
    int n = 10;
    int *ptr1=&n;
    int **ptr2=&ptr1;
    
    printf("Address of n : %u\n",&n);
    printf("Address of n : %u\n",ptr1);
    printf("Address of n : %u\n",ptr2);

}