import random


def guessNumberOp(customNumber):
    if customNumber < surprisenumber:
        message = "The Number is too low"
    if customNumber > surprisenumber:
        message = "The Number is too High"
    if customNumber == surprisenumber:
        message = "The Number is exactly right!"
    return message


print("We are going to guess a number between 1 and 30, Please try to find it")
surprisenumber = random.randint(1, 30)


guessnumber = input("Please Enter the number to guess or exit for ending the game: ")
earlyexit = "FALSE"
if guessnumber != "exit":
    guessingsteps = []
    guessingsteps.append(guessnumber)
    earlyexit = "TRUE"
while guessnumber != "exit":
    result = guessNumberOp(int(guessnumber))
    print(result)
    if result == "The Number is exactly right!":
        break
    else:
        guessnumber = input("Please Enter the number to guess or exit for ending the game: ")
        if guessnumber != "exit":
            guessingsteps.append(guessnumber)

print("This is the list of guessing steps that you tried: ")
newfile = open("GuessingSteps.txt", "w+")
newfile.write("This is the list of guessing steps that you tried: \r\n")
if earlyexit == "TRUE":
    for i in guessingsteps:
        print(i)
        newfile.write("You guessed: " + str(i) + "\r\n")
    if guessnumber == "exit":
        print("The number you were looking for was: " + str(surprisenumber))
        newfile.write("Number you were looking for was:" + str(surprisenumber))
else:
    print("It is too sad that you didn´t want to play")
    print("The number ready for being discovered was: " + str(surprisenumber))
    newfile.write("It is too sad that you didn´t want to play" + "\r\n")
    newfile.write("Number you were looking for was: " + str(surprisenumber))

newfile.close()
