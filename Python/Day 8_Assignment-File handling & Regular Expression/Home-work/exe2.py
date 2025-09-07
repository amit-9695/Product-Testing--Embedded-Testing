# seek() method
# The seek() method changes the file cursor position to a specified location.

f=open('test.txt', 'r')
print("Name of the File : ",f.name)
f.seek(1)
print(f.readline())
f.seek(0)
print(f.readline())
f.close()
