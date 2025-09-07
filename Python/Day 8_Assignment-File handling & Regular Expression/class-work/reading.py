# To read total data from the file --->  read()
with open('test2.txt', 'r') as file:
    data = file.read()
    print(data)
    
print("================================================>")    
# To read 'n' characters from the file --->  read(n)
with open('test2.txt', 'r') as file:
    data = file.read(5)  # Read first 5 characters
    print(data)
    
print("================================================>")
# To read only one line from the file --->  readline()
with open('test2.txt', 'r') as file:
    line = file.readline()  # Read first line
    print(line)
    
print("================================================>")
# To read all lines from the file as a list --->  readlines()
with open('test2.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    print(lines)
    

print("================================================>")
#  to print all the lines without spaces
f=open('test2.txt','r')
lines=f.readlines()
for line in lines:
   print(line,end='')
f.close()
