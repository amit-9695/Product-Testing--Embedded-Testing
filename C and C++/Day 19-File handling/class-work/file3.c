# include<stdio.h>
#include<ctype.h>

void main(){
    FILE *fp = fopen("text.txt", "r");
    char ch;
    int char_count = 0, word_count = 0, line_count = 0;
    int in_word = 0;
    if (fp == NULL) {
        printf("Error opening file.\n");
    }
    else{
        ch=fgetc(fp);
        while(ch != EOF) {
            char_count++;
            if (ch == '\n') {
                line_count++;
            }
            if (isspace(ch)) {
                in_word = 0;
            } else  if (!in_word) {
                in_word = 1;
                word_count++;
            }
            ch = fgetc(fp);
        }
        fclose(fp);
        printf("Characters: %d\n words: %d\n  Lines: %d\n", char_count, word_count, line_count);
    }
}