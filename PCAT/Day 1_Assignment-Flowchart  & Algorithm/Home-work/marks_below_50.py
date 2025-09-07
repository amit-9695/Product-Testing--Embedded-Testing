# Input 40 marks. Count and print how many marks are below 50.
marks = []
for i in range(40):
    mark = float(input("Enter mark {}: ".format(i + 1)))
    marks.append(mark)
below_50 = [mark for mark in marks if mark < 50]
print("Number of marks below 50:", len(below_50))
