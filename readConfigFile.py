def readConfigFile(filename, searchTag, sFunc=""):
    searchTag = searchTag.lower()
    # print("Search Tag: ",searchTag)

    # Open the file
    with open(filename, "r") as filestream:
        # Loop through each line in the file

        for line in filestream:

            if line[0] != "#":

                currentLine = line
                equalIndex = currentLine.find('=')
                if equalIndex != -1:

                    tempLength = len(currentLine)
                    # print("{} {}".format(equalIndex,tempLength))
                    tempIndex = equalIndex
                    configTag = currentLine[0:(equalIndex)]
                    configTag = configTag.lower()
                    configTag = configTag.strip()
                    # print(configTag)

                    configField = currentLine[(equalIndex + 1):]
                    configField = configField.strip()
                    # print(configField)

                    # print("{} {}".format(configTag,searchTag))
                    if configTag == searchTag:

                        # Split each line into separated elements based upon comma delimiter
                        # configField = configField.split(",")

                        # Remove the newline symbol from the list, if present
                        lineLength = len(configField)
                        lastElement = lineLength - 1
                        if configField[lastElement] == "\n":
                            configField.remove("\n")
                        # Remove the final comma in the list, if present
                        lineLength = len(configField)
                        lastElement = lineLength - 1

                        if configField[lastElement] == ",":
                            configField = configField[0:lastElement]

                        lineLength = len(configField)
                        lastElement = lineLength - 1

                        # Apply string manipulation functions, if requested (optional argument)
                        if sFunc != "":
                            sFunc = sFunc.lower()

                            if sFunc == "listout":
                                configField = configField.split(",")

                            if sFunc == "stringout":
                                configField = configField.strip("\"")

                            if sFunc == "int":
                                configField = int(configField)

                            if sFunc == "float":
                                configField = float(configField)

                        filestream.close()
                        return configField

        filestream.close()
        return "Searched term could not be found"

# configFile = "config.cfg"
# dutModel = readConfigFile(configFile, "dutModel", sFunc="strip")
#
# # print(dutModel)
#
# fromConfig = readConfigFile(configFile,"linSteps", "listOut")
# print(fromConfig)
#
# test = [x.strip() for x in fromConfig]
# test2 = [int(x) for x in test]
# print(test2)

# procDirectory = readConfigFile(configFile, "procDirectory", "stringout")
