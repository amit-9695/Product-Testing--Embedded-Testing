""" Program 1:-
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
•	Age is greater than 20
•	Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if
•	Age and marks are valid and
•	Marks is 65 or more
Write a python program to represent the students seeking admission in the university.
The details of student class are given below.
Class name: Student
"""
class Student:
    def __init__(self, student_id, age, marks):
        self.student_id = student_id
        self.age = age
        self.marks = marks

    def is_valid(self):
        return self.age > 20 and 0 <= self.marks <= 100

    def qualifies_for_admission(self):
        return self.is_valid() and self.marks >= 65

    def __str__(self):
        return f"Student ID: {self.student_id}, Age: {self.age}, Marks: {self.marks}"
    
# Example usage
if __name__ == "__main__":
    student1 = Student("S001", 21, 70)
    student2 = Student("S002", 19, 85)
    student3 = Student("S003", 22, 60)

    for student in [student1, student2, student3]:
        print(student)
        if student.qualifies_for_admission():
            print("Status: Qualified for Admission")
        else:
            print("Status: Not Qualified for Admission")
        