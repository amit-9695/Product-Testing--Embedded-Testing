""" Implement a program to display the geometric sequence as given below for a given value n, where n is the number of elements in the sequence.
1, 2, 4, 8, 16, 32, 64, ......, 1024
 """
num = int(input("Enter the number of elements in the geometric sequence: "))
sequence = 1/2
for i in range(num):
    sequence *= 2
    print(int(sequence),end=' ')