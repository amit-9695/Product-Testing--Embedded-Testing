#include<stdio.h>
int main(){
    char str[5]={'a','b','c'};
    for (int i=0; i<5; i++){
        printf("position [%d] = %c\n", i, str[i]);
    }
}