// Finding the root of a quadratic equation
// using the quadratic formula - x = (-b ± √(b² - 4ac)) / 2a
#include <stdio.h>
#include<math.h>

int main(){
    double a,b,c,discriminant,root1,root2,realPart,imagPart;
    printf("Enter First coefficient (a): ");
    scanf("%lf", &a);
    printf("Enter Second coefficient (b): ");
    scanf("%lf", &b);
    printf("Enter Third coefficient (c): ");
    scanf("%lf", &c);

    discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Roots are real and different.\n");
        printf("Root 1 = %.2lf\n", root1);
        printf("Root 2 = %.2lf\n", root2);
    }
    else if (discriminant == 0) {
        root1 = root2 = -b / (2 * a);
        printf("Roots are real and the same.\n");
        printf("Root 1 = Root 2 = %.2lf\n", root1);
    }
    else {
        realPart = -b / (2 * a);
        imagPart = sqrt(-discriminant) / (2 * a);
        printf("Roots are complex and different.\n");
        printf("Root 1 = %.2lf + %.2lfi\n", realPart, imagPart);
        printf("Root 2 = %.2lf - %.2lfi\n", realPart, imagPart);
    }
    return 0;

}