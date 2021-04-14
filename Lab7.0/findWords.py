
def countWords(txtFile, wordToCount):
    count = 0
    for i in txtFile.split():
        if wordToCount == i:
            count = count + 1
    return count


print("Program for counting words into a giveng file")

while True:
    try:
        filetoread = input("Please Enter the name of the file to Analize: ")
        myfile = open(filetoread, mode="r")
        data = myfile.read()
    except FileNotFoundError:
        print("Sorry the file was not found, please enter the name of the file: ")
    else:
        myfile.close()
        break

wordtofind = input("Please Enter the word to count, exit for ending: ")
listofwords = []
listofwords.append(wordtofind)
while wordtofind != "exit":
    wordtofind = input("Please Enter the word to count, exit for ending: ")
    if wordtofind != "exit":
        listofwords.append(wordtofind)

for i in listofwords:
    result = countWords(data, i)
    print("The word " + i + " can be found " + str(result) + " times in the file " + filetoread)
