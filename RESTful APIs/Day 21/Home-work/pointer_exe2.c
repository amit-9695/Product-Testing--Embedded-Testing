# include<stdio.h>
void main(){
    int n =50;
    int *p=&n;
    printf("Address of N %u \n",&n);
    printf("Value of p Variable %d \n",*p);
    printf("Adress of p variable %u",p);
}