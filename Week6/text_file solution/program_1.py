# Read Python.txt file and Print it in Reverse.
file="C:\sqlite3\python.txt"
with open(file,"r")as text_file:
    data=text_file.read()
reverse=data[::-1]
print(reverse)

    




