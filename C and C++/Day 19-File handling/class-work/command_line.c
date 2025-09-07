# include<stdio.h>

int mmain(int argc, char *argv[]) {
    printf("Number of arguments: %d\n", argc);

    for (int i = 0; i < argc; i++) {
        printf("Argument [%d]: %s\n", i, argv[i]);
    }
    return 0;
}

    