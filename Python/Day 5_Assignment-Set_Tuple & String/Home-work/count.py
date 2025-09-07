# A python program to count the number of words in a string.

word=input('enter string ')
word_list=word.split()
count=0
for w in word_list:
    print(w)
    count+=1
print('Total Word:-',count)
