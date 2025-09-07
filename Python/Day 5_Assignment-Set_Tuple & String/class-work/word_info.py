""" 
1. Finding the total number of words
2. find the smallest word
3. Longest word
"""

word="My name is Amit Shukla"

def word_info(word):
    total_word=0
    word_list=word.split(" ")
    smallest_word=word_list[0]
    longest_word = word_list[0]
    for word in  word_list:
        total_word=total_word+1
    
        if len(word)<len(smallest_word):
            smallest_word=word
        if len(word)>len(longest_word):
            longest_word=word
    print(f"smallest word:-  {smallest_word} and  largest word: {longest_word}")
    print(f"Total words:- {total_word}")
            
word_info(word)
