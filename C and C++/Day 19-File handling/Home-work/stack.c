#include <stdio.h>
#define SIZE 5

// Global array and top pointer for the stack
int stack[SIZE];
int top = -1;

// Function to add an element to the top of the stack (push)
void push(int value) {
    // Check for stack overflow
    if (top == SIZE - 1) {
        printf("Stack Overflow! Cannot push %d.\n", value);
    } else {
        top++;
        stack[top] = value;
        printf("Pushed %d onto the stack.\n", value);
    }
}

// Function to remove an element from the top of the stack (pop)
void pop() {
    // Check for stack underflow
    if (top == -1) {
        printf("Stack Underflow! Cannot pop.\n");
    } else {
        printf("Popped %d from the stack.\n", stack[top]);
        top--;
    }
}

// Function to display the elements of the stack
void display() {
    if (top == -1) {
        printf("Stack is empty.\n");
    } else {
        printf("Stack elements are: ");
        // Iterate from top to bottom
        for (int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

// Main function to demonstrate stack operations
int main() {
    printf("--- Stack Operations ---\n");
    display();
    
    push(10);
    push(20);
    push(30);
    display();
    
    pop();
    display();
    
    push(40);
    push(50);
    push(60); // This will cause an overflow
    display();
    
    pop();
    pop();
    pop();
    pop();
    pop(); // This will cause an underflow
    display();
    
    return 0;
}
