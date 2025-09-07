# include<stdio.h>
# define SQUARE(x) ((x) * (x))  // Define a macro to calculate the square of a number

int main() {
    int num = 5;
    int result = SQUARE(num);  // Use the macro to calculate the square of num
    printf("The square of %d is %d\n", num, result);
    return 0;
}