def readTxtFile(filename,searchTag,index, sFunc=""):
    # Example Useage:
    # emailList = readTxtFile(templateFile, "emails", "1:", sFunc="list")
    # Returns values as a list
    
    indexing = False
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
                    indexing = True
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

                    if sFunc == "strip" and indexing == False:
                        output = output.strip()

                if (type(output) is list) and sFunc != "list":
                    output2 = ""
                    for i in output:
                        output2 += str(i) + ","
                    length = len(output2)
                    output2 = output2[0:(length-1)]
                    output = ""
                    output = output2
                    
                if (type(output) is str) and sFunc == "list":
                    output = output.split(",")

                return output

        return "Searched term could not be found"


    filestream.close()
    return "Searched term could not be found"
# templateFile = "C:\\Users\\Micah\\PycharmProjects\\TimebaseMonitor\\TBMconfig.ini"
# lookup = "timeBase1"
# tbDevice = readTxtFile(templateFile, lookup, "1:", sFunc="strip")
#
# print(tbDevice)
# print(type(tbDevice))