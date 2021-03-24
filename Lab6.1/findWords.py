import re


def countWords(txtFile, wordToCount):
    count = 0
    for i in txtFile.split():
        if wordToCount == i:
            count = count + 1
    return count


print("Program for counting words into a giveng file")

while True:
    try:
        fileToRead = input("Please Enter the name of the file to Analize: ")
        myFile = open(fileToRead, mode="r")
        data = myFile.read()
    except FileNotFoundError:
        print("Sorry the file was not found, please enter the name of the file: ")
    else:
        myFile.close()
        break

wordToFind = input("Please Enter the word to count, exit for ending: ")
listOfWords = []
listOfWords.append(wordToFind)
while wordToFind != "exit":
    wordToFind = input("Please Enter the word to count, exit for ending: ")
    if wordToFind != "exit":
        listOfWords.append(wordToFind)

for i in listOfWords:
    result = countWords(data, i)
    print("The word " + i + " can be found " + str(result) + " times in the file " + fileToRead)
