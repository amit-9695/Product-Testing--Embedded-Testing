# Input a mark. Calculate and output a student's grade;

# 80 < A <= 100
# 60 < B <= 80
# 40 < C <= 60
# 0 <= U <= 40
mark = float(input("Enter the mark: "))
if 80 < mark <= 100:
    grade = 'A'
elif 60 < mark <= 80:
    grade = 'B'
elif 40 < mark <= 60:
    grade = 'C'
else:
    grade = 'U'
print("The grade is:", grade)
