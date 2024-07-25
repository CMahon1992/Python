#opens the file as read only mode
with open('myFile.txt', 'r') as file:
    content = file.read() #reads the entire file as a string
    print(content)

#writing a new file
with open('newFile.txt', 'w') as f:
    f.write("Today was a good day.\n")
    f.write("Welcome to the hotel of California.\n")

with open('newFile.txt', 'r') as new:
    readNewFile = new.read()
    print(readNewFile)

#appending text to a file
with open('newFile.txt','a') as addText:
    addText.write('Such a lovely place.\n')
with open('newFile.txt', 'r') as new:
    readNewFile = new.read()
    print(readNewFile)

#writing a new file
with open('iDoNotExist.txt','w') as x:
    x.write("Hey, I do exist!")
with open('iDoNotExist.txt', 'r') as z:
    pleaseRead = z.read()
    print(pleaseRead)

