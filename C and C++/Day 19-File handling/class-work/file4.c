#include<stdio.h>

void main() {
    FILE *fp = fopen("text.txt", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
    } else {
        fseek(fp, 0, SEEK_END); // Move to the end of the file
        long file_size = ftell(fp); // Get the current position (file size)
        rewind(fp); // Move back to the beginning of the file
        printf("File size: %ld bytes\n", file_size);
        fclose(fp);
    }
}