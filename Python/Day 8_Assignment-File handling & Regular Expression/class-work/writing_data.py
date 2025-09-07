f=open('test2.txt','w')
f.write('GET')
f.write('SET')
f.write('TECH')
print('Data Written Successfully')
f.close()

# Python doesn't automatically add line breaks, you need to do that manually by using---\n

f=open('test3.txt','w')
f.write('\nGET')
f.write('\nSET')
f.write('\nTECH')
print('Data Written Successfully')
f.close()

# if we want to append data to the file, we can use 'a' mode
f=open('test2.txt','a')
f.write('\n Appended Data')
print('Data Appended Successfully')
f.close()
