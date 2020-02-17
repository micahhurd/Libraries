def readUncFile(filename,x,y,function=""):
    xFind = x
    yFind = y
    if function == "":
        function = "null"

    filestream = open(filename, 'r')                    # Open specified uncertainty file
    filestreamLines = filestream.readlines()            # Create a list of all lines from the uncertainty file
    filestream.close()

    # Remove any blank lines from the list of file lines
    j = 0
    for i in filestreamLines:
        if i == "\n":
            del filestreamLines[j]
        j += 1


    # This for loop will search for the desired measurement function and find the start and ending lines of that
    # function. It will also determine if the function contains multiple x axis ranges
    functionStartLine = 0
    functionEndLine = 0
    functionStartFound = False
    functionEndFound = False
    j = 0                                               # Line counter
    for i in filestreamLines:                           # Enumerate through each line in the line list
        currentLine = i.split(",")                      # Split out the currently enumerated line according to CSV
        lineName = str(currentLine[0])                  # Obtain the line tag name

        index = 1                                       # Default index to 1 for cases where there are no ranged uncertainties
        check = ":" in lineName                         # look to see if line has the "function flag", which is ":"
        if check == True:
            if function == "null" and functionStartFound == False:
                xVals = currentLine[1:]  # Place the contents (ranges) of the function line to variable
                functionStartLine = j  # note the line number of the function start line
                functionStartFound = True  # Mark the flag indicating the the starting line was found
                index = j
                # print("xVals: {}".format(xVals))

            check = function in lineName                # Check to see if the specified function matches the line
            # print("check: {}".format(check))
            if check == True and functionStartFound == False:
                xVals = currentLine[1:]                 # Place the contents (ranges) of the function line to variable
                # print("xVals: " + str(xVals))
                functionStartLine = j                   # note the line number of the function start line
                functionStartFound = True               # Mark the flag indicating the the starting line was found
            else:
                if functionStartFound == True and j != index:            # If a colon was found and the specified function is found already
                    functionEndLine = j - 1                 # End of desired function is start of next function minus 1 line
                    functionEndFound = True                 # Mark the flag indicating the end of the function has been found

        if functionStartFound == True and functionEndFound == True:
            break                                       # Break out of the enumeration once the function line boundaries are found

        j += 1                                          # Increment the line counter

    if functionStartFound == True and functionEndFound == False:
        fileLength = len(filestreamLines)
        functionEndLine = fileLength
        functionEndFound = True

    # This logic will compared the desired x value passed into this function to the xVals found above, and
    # determine the x index for uncertainty files which contain ranged uncertainty values
    xValsLen = len(xVals)  # Determine the quantity of X ranges in the uncertainty file
    # print("xVals: " + str(xVals))
    # print("xValsLen: " + str(xValsLen))
    if xValsLen == 1:
        xIndex = 1                                      # For files which are not multiranged, the index is 1
    else:
        j = 1
        for i in xVals:
            range = i.split(":")                        # split out the upper and lower bounds of the range
            lower = float(range[0])
            upper = float(range[1])
            # print("lower: " + str(lower))
            # print("upper: " + str(upper))
            # print("xFind: " + str(xFind))
            if xFind >= lower and xFind <= upper:       # test against the upper and lower range boundaries
                xIndex = j                              # take down the x Index if a range matches
                # print("xIndex1: " + str(xIndex))
                break
            else:
                xIndex = 0                              # Set to zero if no ranges matched
            j += 1
    # print("xIndex2: " + str(xIndex))

    # This loop will find the line which contains the specified uncertainty according to the y axis value given
    # it does this by comparing the desired y value (passed into this function) according to the y value of each line.
    # If finds the line which is equal to, or has the smallest difference from, the desired y value, and that becomes
    # the correct line for pulling out the uncertainty, noted a yIndex
    # print("functionStartLine: {}".format(functionStartLine))
    # print("functionEndLine: {}".format(functionEndLine))
    j = 0
    for i in filestreamLines:                           # Enumerate through the lines of the file
        if j > functionStartLine and j <= functionEndLine:  # Only look at values which are within the function field
            currentLine = i.split(",")                  # Convert the current line to a list based on csv
            yVal = float(currentLine[0])                # Take the y value (first element of this list) as a float
            # print("Y Value: {}".format(yVal))
            diff = abs(yFind - yVal)                         # find the difference between the current y value and the desired y Value
            if yFind == yVal:                           # if they are equal then the correct line of the uncertainty file is found
                yIndex = j                              # take the index of the line
                break                                   # break out of the loop early
            else:
                try:
                    diffDelta                           # see if diffDelta variable has been declared yet or not
                    # print(22)
                except NameError:                       # If not then set the initial diff delta value
                    diffDelta = diff
                    yIndex = j
                    # print(23)
                else:
                    # print(24)
                    if diff < diffDelta:                # Compare the current diff to the diff Delta
                        diffDelta = diff                # If smaller than update the diffDelta
                        yIndex = j                      # note the index of the current line
        j += 1

    # This string will pull the uncertainty using the x and y index values which have been determined already
    if xIndex == 0:                                     # in this case the range was not found
        unc = 0
    else:
        currentLine = filestreamLines[yIndex]
        currentLine = currentLine.split(",")
        unc = currentLine[xIndex]

    return unc


# uncFileName = "uncTestFile.txt"
# result = readUncFile(uncFileName,0,0,"rho")
#
# print("Unc result {}".format(result))