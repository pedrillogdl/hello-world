
def countingDigits(intNumber):
    count = 0
    while intNumber >= 1:
        intNumber = intNumber / 10
        count = count + 1
    return count


def int_to_str(numberToString):
    intToStr = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    stringNumber = ""
    totalDigits = countingDigits(numberToString)
    position = countingDigits(numberToString) - 1
    count = 0
    while count < totalDigits:
        i = numberToString // (10**position)
        numberToString = numberToString - (i*(10**position))
        for x in intToStr:
            if i == x:
                i = intToStr[x]
                break
        stringNumber = stringNumber + i
        count = count + 1
        position = position - 1
    return stringNumber


def validate_char(numberToValidate):
    strToInt = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for i in numberToValidate:
        findChar = "FALSE"
        for x in strToInt:
            if i == x:
                findChar = "FALSE"
                break
            if x == "9" and i != x:
                findChar = "TRUE"
                break
        if findChar == "TRUE":
            isChar = "TRUE"
            break
        else:
            isChar = "FALSE"
    return isChar


def str_to_int(stringToNumber):
    validateChar = validate_char(stringToNumber)
    if validateChar == "TRUE":
        return None
    strToInt = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    position = len(stringToNumber) - 1
    intNumber = 0
    for i in stringToNumber:
        for x in strToInt:
            if i == x:
                i = strToInt[x]
                break
        intNumber = intNumber+(i*(10**position))
        position = position - 1
    return intNumber


print("Program for converting a string to integer and viceversa\r\n")


while True:
    try:
        numbertoconvert = str_to_int(input("Please Enter the number to convert: "))
        if numbertoconvert is None:
            nonumber = -1
        else:
            nonumber = 1
        assert nonumber > 0
    except AssertionError:
        print("Please enter a number, characters are not accepted")
    else:
        break


result = numbertoconvert
typenumbertoconvert = type(numbertoconvert)
typestringtonumber = type(result)

print(f"The number   {numbertoconvert}  was a <class 'str'>  now it is a {typestringtonumber}\r\n")
print("Do you want to conver again the number from int to string?")
answer = input("Enter yes for converting the number back or no for exiting the program: ")
if answer == "yes":
    resultint = int_to_str(result)
    typenumbertoconvert = type(result)
    typenumbertostring = type(resultint)
    print(f" \r\nThe number   {resultint}  was a {typenumbertoconvert}  now it is a {typenumbertostring}")
else:
    print("\r\nToo bad you don´t want to convert back the number")
