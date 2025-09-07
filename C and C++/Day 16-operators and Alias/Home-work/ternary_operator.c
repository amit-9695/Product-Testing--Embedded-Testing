// Program that takes input of a student's marks and use ternary operator to determine if the student has passed or failed
#include <stdio.h>
#include <stdlib.h>
int main() {
    int marks;
    printf("Enter student's marks: ");
    scanf("%d", &marks);
    // Using ternary operator to check if the student has passed or failed
    printf("The student has %s\n", (marks >= 40) ? "passed" : "failed");
    return 0;
}