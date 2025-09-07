//  Program to read first line from a file
#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *file;
    char line[256];
    // Open the file in read mode
    file = fopen("example.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    // Read the first line from the file
    if (fgets(line, sizeof(line), file) != NULL) {
        printf("First line: %s", line);
    }
    // Close the file
    fclose(file);
    return EXIT_SUCCESS;
}
