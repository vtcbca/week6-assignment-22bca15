 # Read Python.txt file and Print unique word with its count.
unique_words_count=0
with open("c:\\sqlite3\\python.txt","r") as file:
        line=file.read()
        words=set(line.split())
print("total unique words:",len(words))
print("Unqiue words are:",words)

