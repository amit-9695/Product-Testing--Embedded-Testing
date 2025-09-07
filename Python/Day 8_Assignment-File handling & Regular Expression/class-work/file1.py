f= open('test.txt','r')
if f:
    print("File opened successfully")
else:
    print("File not found")
f.close()
