#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1;
int rear = -1;

// Function to check if the queue is full
int isFull() {
    if (rear == SIZE - 1) {
        return 1;
    }
    return 0;
}

// Function to check if the queue is empty
int isEmpty() {
    if (front == -1 || front > rear) {
        return 1;
    }
    return 0;
}

// Function to add an element to the queue (enqueue)
void enqueue(int value) {
    if (isFull()) {
        printf("Queue is full. Cannot enqueue %d.\n", value);
    } else {
        if (front == -1) {
            front = 0; // Set front to the first position
        }
        rear++;
        queue[rear] = value;
        printf("Enqueued %d to queue.\n", value);
    }
}

// Function to remove an element from the queue (dequeue)
int dequeue() {
    int item;
    if (isEmpty()) {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1; // Return -1 to indicate an error or empty queue
    } else {
        item = queue[front];
        front++;
        // If the last element was dequeued, reset the queue
        if (front > rear) {
            front = -1;
            rear = -1;
        }
        printf("Dequeued %d from queue.\n", item);
        return item;
    }
}

// Function to get the front element of the queue without removing it
int peek() {
    if (isEmpty()) {
        printf("Queue is empty.\n");
        return -1; // Return -1 to indicate an error or empty queue
    }
    return queue[front];
}

// Function to display all the elements in the queue
void display() {
    if (isEmpty()) {
        printf("Queue is empty.\n");
    } else {
        printf("Queue elements are: ");
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}

// Main function to demonstrate queue operations
int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();

    printf("Front element is %d\n", peek());

    dequeue();
    display();

    enqueue(40);
    enqueue(50);
    display();
    
    // This will show the queue is full
    enqueue(60);

    dequeue();
    dequeue();
    dequeue();
    dequeue();
    display(); // Queue should be empty now

    // This will show the queue is empty
    dequeue();

    return 0;
}
