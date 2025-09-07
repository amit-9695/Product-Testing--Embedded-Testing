// Program to read all lines from a file
#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *file;
    char line[256];
    // Open the file in read mode
    file = fopen("example2.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    // Read all lines from the file
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }
    // Close the file
    fclose(file);
    return EXIT_SUCCESS;
}   