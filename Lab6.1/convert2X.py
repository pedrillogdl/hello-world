
def convertBinary(decimalNumber):
    binaryNumber = []
    rightBinaryNumber = []
    leftover = decimalNumber
    while leftover != 1:
        binaryNumber.append(leftover % 2)
        leftover = leftover // 2
    binaryNumber.append(leftover)
    for i in binaryNumber:
        rightBinaryNumber.insert(0, i)
    return rightBinaryNumber


def convertHexadecimal(decimalNumber):
    hexaNumber = []
    rightHexaNumber = []
    leftoverNumber = decimalNumber
    while leftoverNumber > 15:
        hexaNumber.append(leftoverNumber % 16)
        leftoverNumber = leftoverNumber // 16
    hexaNumber.append(leftoverNumber)
    for i in hexaNumber:
        if i == 10:
            i = "A"
        if i == 11:
            i = "B"
        if i == 12:
            i = "C"
        if i == 13:
            i = "D"
        if i == 14:
            i = "E"
        if i == 15:
            i = "F"
        rightHexaNumber.insert(0, i)
    return rightHexaNumber


print("Converting a decimal number into a binary and hexadecimal number")

while True:
    try:
        numberToConvert = int(input("Please Enter the number to convert: "))
        assert numberToConvert >= 0
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except AssertionError:
        print("Please enter a number bigger or equal to 0")
    else:
        break

if numberToConvert == 0:
    finalBinaryNumber = 0
    finalHexaNumber = 0
else:
    result = convertBinary(numberToConvert)
    resultHexa = convertHexadecimal(numberToConvert)
    finalBinaryNumber = ' '.join([str(elem) for elem in result])
    finalHexaNumber = ' '.join([str(elem) for elem in resultHexa])

print("The number " + str(numberToConvert) + " converted to binary is: " + str(finalBinaryNumber))
print("The number " + str(numberToConvert) + " converted to hexadecimal is: " + str(finalHexaNumber))
