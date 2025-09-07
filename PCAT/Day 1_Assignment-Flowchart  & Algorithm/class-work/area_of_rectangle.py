# # Input the length L and the breadth B, calculate and output the area of a rectangle.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
def area_of_rectangle(length, breadth):
    area = length * breadth
    return area

area = area_of_rectangle(length, breadth)
print("The area of the rectangle is:", area)    