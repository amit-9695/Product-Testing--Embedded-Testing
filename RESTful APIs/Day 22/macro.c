# include <stdio.h>
# define SQUARE(x) x * x

int main() { 
    printf("%d\n", SQUARE(3+1)); // This will expand to 3+1 * 3+1---> 7
    printf("%d\n", SQUARE(3)); // This will expand to 3 * 3---> 9
    printf("%d\n", SQUARE(3+1) + 2); // This will expand to 3+1 * 3+1 + 2---> 9
    printf("%d\n", SQUARE(3) + 2); // This will expand to 3 * 3 + 2---> 11
    
    return 0;
}