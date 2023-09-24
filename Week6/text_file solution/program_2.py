# Read Python.txt file and Print total number of lines and words in it.
number_words=0
with open("c:\\sqlite3\\python.txt","r") as file:
    for line in file:
        words=line.split()
        number_words+=len(words)
with open("c:\\sqlite3\\python.txt","r") as file:
    lines=file.readlines()
total_lines=len(lines)
print("Total number of lines:",total_lines)
print("Total number of words:",number_words)
