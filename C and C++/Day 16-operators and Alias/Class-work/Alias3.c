#include <stdio.h>
 
typedef struct {
    int id;
    char name[50];
} Employee;
 
int main() {
    Employee e1 = {101, "Ashish"};
    printf("Employee ID: %d, Name: %s\n", e1.id, e1.name);
    return 0;
}