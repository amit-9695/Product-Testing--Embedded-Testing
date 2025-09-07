#include <stdio.h>
 
typedef int* IntPtr;
 
int main() {
    int a = 10;
    IntPtr p = &a;  // same as: int* p = &a;
    printf("Value via pointer: %d\n", *p);
    return 0;
}