import random

def readTxtFile(filename,searchTag,index, sFunc=""):
    searchTag = searchTag.lower()
    # print("Search Tag: ",searchTag)

    # Open the file
    with open(filename, "r") as filestream:
        # Loop through each line in the file
        for line in filestream:
            # Split each line into separated elements based upon comma delimiter
            currentLine = line.split(",")
            # select the first comma seperated value
            search = str(currentLine[0])
            # Set the value to all lowercase for comparison
            search = search.lower()

            # Remove the newline symbol from the list, if present
            lineLength = len(currentLine)
            lastElement = lineLength - 1
            if currentLine[lastElement] == "\n":
                currentLine.remove("\n")
            lineLength = len(currentLine)
            lastElement = lineLength - 1

            # Output the line which matches the search
            # If index is populated then output the indexed field
            if search == searchTag:
                if index == "":
                    output = currentLine
                    # break
                    # return currentLine

                if type(index) is int:
                    if index > lineLength:
                        output = "Index out of range"
                        # break
                    else:
                        output = currentLine[index]
                        # break
                        # return currentLine[index]

                if type(index) is str and index.find(":"):
                    index = index.split(":")
                    index[0] = int(index[0])

                    if index[0] > lineLength:
                        output = "Index out of range"
                        # break
                        # return "Index out of range"

                    if index[1] != "" and index[1] != " ":
                        index[1] = int(index[1])
                        if index[1] > lineLength:
                            output = "Index out of range"
                            # break
                            # return "Index out of range"

                    if index[1] == "" or index[1] == " ":
                        index[1] = lastElement

                    parsedLine = []
                    while index[0] <= index[1]:
                        x = currentLine[index[0]]
                        parsedLine.append(x)
                        index[0] += 1
                    output = parsedLine
                    # break
                    #return parsedLine.

                # Apply string manipulation functions, if requested (optional argument)
                if sFunc != "":
                    sFunc = sFunc.lower()

                    if sFunc == "strip":
                        output = output.strip()
                    elif sFunc == "float":
                        output = output.strip()
                        output = float(output)
                    elif sFunc == "whole":
                        output = output.strip()
                        output = int(output)

                filestream.close()
                return output
        filestream.close()
        return "Searched term could not be found"

    filestream.close()
    return "Searched term could not be found"

def visaResourceSim(deviceName):

    print("Detected VISA resources (sim)")
    print("=========================================================")

    resources = ["Sim GPIB", "Sim USB ", "Sim Serial", "Sim Visa"]
    x = 0
    for i in resources:  # Enumerate through list "resources"
        print('Resource ' + str(x) + ': ' + str(i))  # Print each resource contained in list "resources"
        x += 1  # X is used to itemize and index the list that gets printed
    print("=========================================================")
    x = x - 1

    address = -1
    while (address < 0) or (address > (x)):
        try:
            address = int(input(
                " > Enter the resource number of the " + str(deviceName) + " (0 through " + str(x) + "): "))
        except ValueError:
            print("No valid integer entered! Please try again ...")
        if address < 0 or address > (x):
            print("Available resources are 0 through " + str(x) + ". Please try again.")

    inst = resources[address]
    return inst

def queryVisaSim(instrument, command, sFunc=""):
    visaSimCommands = "visaSimCommands.txt"


    command = str(command)
    command = command.lower()
    check = "fetch?" in command
    check2 = ":" in command

    if command == "*idn?":
        return instrument
    elif command == "*opc?":
        return "1"
    elif check == True or check2 == True:
        complexCommand = command.split(":")
        if check == True and check2 == False:
            return "0.1"
        if check == True and check2 == True:
            number = int(complexCommand[1])
            randNum = random.randrange(-100, 100, 1)
            randNum = randNum / 100
            number = number + randNum
            return str(number)
        if check == False and check2 == True:
            return "0.1234,1"
    else:
        # returned = readTxtFile(visaSimCommands, "default", "1:")
        #
        # result = ""
        # for i in returned:
        #     result = result + str(i) + ","

        return "0,1"


    # if sFunc != "":
    #     sFunc = sFunc.lower()
    #
    #     if sFunc == "float":
    #         msmt = float(msmt)

def writeVisaSim(instrument, command):
    return 0

# print(queryVisaSim("test",""))
