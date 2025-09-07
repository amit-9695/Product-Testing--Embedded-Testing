# Finding the frequency of characters in a word using dictionary comprehension

word="banana"
frequency = {char: word.count(char) for char in set(word)}
print(frequency)


# Creating a dictionary with word lengths
words=["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)