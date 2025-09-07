# Identify the grade based on the score

marks = int(input("Enter your marks: "))
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"

result= get_grade(marks)
print(f"Your grade is: {result}")