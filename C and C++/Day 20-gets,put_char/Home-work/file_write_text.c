// Program to write a Sentence to a file
#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *fp;
    char sentence[100];
    // Open the file in write mode
    fp = fopen("output.txt", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    // Get the sentence from the user
    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);
    // Write the sentence to the file
    fprintf(fp, "%s", sentence);
    // Close the file
    fclose(fp);
    printf("Sentence written to file successfully.\n");
    return 0;
}