# include <stdio.h>
# define SIZE 5

int stack[SIZE];
int top = -1;

void push(int value) {
    if (top == SIZE - 1) {
        printf("Stack overflow\n");
    } else {
        top++;
        stack[top] = value;
        printf("Pushed %d onto stack\n", value);
    }
}

int pop() {
    if (top == -1) {
        printf("Stack underflow\n");
    } else {
        printf("Popped %d from stack\n", stack[top]);
        top--;
        return stack[top];
    }
}

int peek() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1; // Indicating stack is empty
    } else {
        return stack[top];
    }
}

// Display the stack value
void display() {
    if (top == -1) {
        printf("Stack is empty\n");
    } else {
        printf("Stack elements: ");
        for (int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

// main method
void main() {
    push(10);
    push(20);
    push(30);
    display();
    
    printf("Top element is %d\n", peek());
    
    pop();
    display();
    
    push(40);
    display();
    
    pop();
    pop();
    pop(); 
    pop(); // This will also cause underflow
    display();
}