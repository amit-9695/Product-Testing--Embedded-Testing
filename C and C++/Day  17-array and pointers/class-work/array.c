# include <stdio.h>

# define SIZE 5
int main(){
    int a12rr[SIZE];
    for (int i = 0; i < SIZE; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("You entered: ");
    for (int i = 0; i < SIZE; i++) {
        printf("arr[%d]= %d\n ", i,arr[i]);
    }
}