# include <stdio.h>

void main(){
    int i=0, j=0;
    int arr[4][3]={
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {10, 11, 12}
    };
    for(i = 0; i < 4; i++){
        for(j = 0; j < 3; j++){
            printf("arr[%d][%d]=%d\n ",i,j, arr[i][j]);
        }
        printf("\n");
    }
}