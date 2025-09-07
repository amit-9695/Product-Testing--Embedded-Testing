# tell() method
# The tell() method returns the current position of the file cursor in a file.

f=open('test.txt', 'r')
print("Name of the File : ",f.name)
pos=f.tell()
print("Current Position             : ",pos)
str=f.read(2)
print("Read String is till 2       : ",str)
pos=f.tell()
print("Current Position             : ",pos)
str=f.read(3)
print("Read String is till 2       : ",str)
pos=f.tell()
print("Current Position             : ",pos)
f.close()

