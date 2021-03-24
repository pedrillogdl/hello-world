import random


def guessNumberOp(customNumber):
    if customNumber < surpriseNumber:
        message = "The Number is too low"
    if customNumber > surpriseNumber:
        message = "The Number is too High"
    if customNumber == surpriseNumber:
        message = "The Number is exactly right!"
    return message


print("We are going to guess a number between 1 and 30, Please try to find it")
surpriseNumber = random.randint(1, 30)


guessNumber = input("Please Enter the number to guess or exit for ending the game: ")
earlyExit = "FALSE"
if guessNumber != "exit":
    guessingSteps = []
    guessingSteps.append(guessNumber)
    earlyExit = "TRUE"
while guessNumber != "exit":
    result = guessNumberOp(int(guessNumber))
    print(result)
    if result == "The Number is exactly right!":
        break
    else:
        guessNumber = input("Please Enter the number to guess or exit for ending the game: ")
        if guessNumber != "exit":
            guessingSteps.append(guessNumber)

print("This is the list of guessing steps that you tried: ")
newFile = open("GuessingSteps.txt", "w+")
newFile.write("This is the list of guessing steps that you tried: \r\n")
if earlyExit == "TRUE":
    for i in guessingSteps:
        print(i)
        newFile.write("You guessed: " + str(i) + "\r\n")
    if guessNumber == "exit":
        print("The number you were looking for was: " + str(surpriseNumber))
        newFile.write("Number you were looking for was:" + str(surpriseNumber))
else:
    print("It is too sad that you didn´t want to play")
    print("The number ready for being discovered was: " + str(surpriseNumber))
    newFile.write("It is too sad that you didn´t want to play" + "\r\n")
    newFile.write("Number you were looking for was: " + str(surpriseNumber))

newFile.close()
