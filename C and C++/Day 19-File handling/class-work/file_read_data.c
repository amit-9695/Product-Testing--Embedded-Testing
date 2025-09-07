# include<stdio.h>

void main() {
    FILE *fp = fopen("text.txt", "r");
    char buffer[100];
    if (fp == NULL) {
        printf("Error opening file.\n");
    } 
    else {
        while(fgets(buffer, sizeof(buffer), fp)!= NULL) {
            printf("%s", buffer);
        }
        fclose(fp);
    }
}