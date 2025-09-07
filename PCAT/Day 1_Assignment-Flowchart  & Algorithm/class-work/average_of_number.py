# Enter 20 marks and print their average.
marks = []
for i in range(20):
    mark = float(input("Enter mark {}: ".format(i + 1)))
    marks.append(mark)
average = sum(marks) / len(marks)
print("The average of the marks is:", average)
