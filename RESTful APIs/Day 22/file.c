#include <stdio.h>
 
int main() {
    FILE *fp;
    int ch;
 
    fp = fopen("sample.txt", "r");
    if (fp == NULL) {
        perror("Unable to open file");
        return 1;
    }
 
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);  // prints one character at a time
    }
 
    fclose(fp);
    return 0;
}