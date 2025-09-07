// Sum of two matrices

# include<stdio.h>

void main(){
    int a[5][5],b[5][5],c[5][5],m,n;
    printf("Enter the number of rows and columns: ");
    scanf("%d %d",&m,&n);
    printf("Enter the elements of first matrix:\n");
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    printf("Enter the elements of second matrix:\n");
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&b[i][j]);
        }
    }
    printf("The sum of the two matrices is:\n");
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            c[i][j] = a[i][j] + b[i][j];
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
}
