# include<stdio.h>

void main() {
    FILE *fp=fopen("example.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
    }

     else{
        fprintf(fp, "Hello, World!\n");
        fputs("This is a test file.\n", fp);
        fclose(fp);
        printf("File written successfully.\n");
     }

}