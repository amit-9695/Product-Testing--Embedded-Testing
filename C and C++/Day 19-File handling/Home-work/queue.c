#include <stdio.h>
#define SIZE 5

// Global array and pointers for the queue
int queue[SIZE];
int front = -1;
int rear = -1;

// Function to add an element to the rear of the queue (enqueue)
void enqueue(int value) {
    // Check if the queue is full
    if (rear == SIZE - 1) {
        printf("Queue is Full! Cannot enqueue %d.\n", value);
    } else {
        // If it's the first element, set front
        if (front == -1) {
            front = 0;
        }
        rear++;
        queue[rear] = value;
        printf("Enqueued %d to the queue.\n", value);
    }
}

// Function to remove an element from the front of the queue (dequeue)
void dequeue() {
    // Check if the queue is empty
    if (front == -1 || front > rear) {
        printf("Queue is Empty! Cannot dequeue.\n");
    } else {
        printf("Dequeued %d from the queue.\n", queue[front]);
        front++;
    }
}

// Function to display the elements of the queue
void display() {
    if (front == -1 || front > rear) {
        printf("Queue is empty.\n");
    } else {
        printf("Queue elements are: ");
        // Iterate from front to rear
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}

// Main function to demonstrate queue operations
int main() {
    printf("--- Queue Operations ---\n");
    display();
    
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    
    dequeue();
    display();
    
    enqueue(40);
    enqueue(50);
    enqueue(60); // This will show the queue is full
    display();
    
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue(); // This will show the queue is empty
    display();
    
    return 0;
}
