
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
        numbertoconvert = int(input("Please Enter the number to convert: "))
        assert numbertoconvert >= 0
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except AssertionError:
        print("Please enter a number bigger or equal to 0")
    else:
        break

if numbertoconvert == 0:
    finalbinarynumber = 0
    finalhexanumber = 0
else:
    result = convertBinary(numbertoconvert)
    resulthexa = convertHexadecimal(numbertoconvert)
    finalbinarynumber = ' '.join([str(elem) for elem in result])
    finalhexanumber = ' '.join([str(elem) for elem in resulthexa])

print("The number " + str(numbertoconvert) + " converted to binary is: " + str(finalbinarynumber))
print("The number " + str(numbertoconvert) + " converted to hexadecimal is: " + str(finalhexanumber))
