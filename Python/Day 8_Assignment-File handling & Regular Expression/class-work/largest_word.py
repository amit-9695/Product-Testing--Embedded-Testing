with open('test.txt', 'r') as file:
    word = file.read().split()
    longest_word = max(word, key=len)
    print(f"The longest word is: {longest_word}")
    print(f"The length of the longest word is: {len(longest_word)}")
    print(f"Total number of words: {len(word)}")
    
# using a different method
with open('test.txt', 'r') as file:
    words = file.read().split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
    print(f"The length of the longest word is: {len(longest_word)}")
    print(f"Total number of words: {len(words)}")