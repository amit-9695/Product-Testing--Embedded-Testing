with open("greeting.txt", "w") as file:
    file.write("Hello, welcome to python file handling!\n")
  
with open("greeting.txt", "r") as file:
    print(file.read())
    
with open("greeting.txt", "a") as file:
    file.write("Enjoy your learning journey!\n")

with open("greeting.txt", "r") as file:
    for line in file:
        print(line.strip())
        
line_count = 0
word_count = 0
char_count = 0
with open("greeting.txt", "r") as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        char_count += len(line)
print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

with open("greeting.txt", "r") as file:
    content = file.read()
    
    with open("destination.txt", "w") as f:
        f.write(content)


with open("destination.txt", "r") as f:
    content = f.read()
    
    with open("destination.txt", "w") as file:
        update=content.replace("journey!", "Content!")
        file.write(update)