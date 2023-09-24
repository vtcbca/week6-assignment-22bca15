#Read Python.txt file and Print largest and smallest word from it.
with open("c:\\sqlite3\\python.txt","r") as file:
        line=file.read()
        words=line.split()
        largest=small=words[0]
        for i in range(0,len(words)):
            if (len(largest)<len(words[i])):
                largest=words[i]
            elif(len(small)>len(words[i])):
                  small=words[i]
print("largest word:",largest)
print("smallest word:",small)
