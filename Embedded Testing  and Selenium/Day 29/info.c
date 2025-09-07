# include<stdio.h>
 void calculate(int a, int b) {
    int sum = a + b;
    int product = a * b;
    printf("Sum: %d,\n  Product: %d\n", sum, product);
 }

 int main() {
    int x = 5, y = 3;
    calculate(x, y);
    return 0;
 }