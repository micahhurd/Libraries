def userPrompt(message,inType="",range=""):
    import os
    # requires import os
    # Example usage:
    # evalMethod = userPrompt("Please enter an option.","num","1:4:whole")
    # userPrompt("Set the step attenuator to {} dB".format(nominal),"")

    def stringInput(prompt):
        a = False
        b = False
        while a == False:
            string = input(" > " + str(prompt) + " ")
            while b == False:
                check = input(" > Please verify that \"{}\" is correct. Enter (y)es or (n)o: ".format(string))
                # print("entered: ",check)
                check = check.lower()
                # print("lowered: ", check)
                if check != "y" and check != "n":
                    print("!! You must enter \"y\" for Yes or \"n\" for No !!")
                elif check == "y" or check == "n":
                    b = True
            if check == "y":
                a = True
            else:
                b = False
        string = string.strip()
        return string

    def yesNoPrompt(prompt):
        b = False
        while b == False:
            check = input(" > "+ str(prompt) + " - Enter (y)es or (n)o: ")
            # print("entered: ",check)
            check = check.lower()
            # print("lowered: ", check)
            if check != "y" and check != "n":
                print("!! You must enter \"y\" for Yes or \"n\" for No !!")
            elif check == "y" or check == "n":
                b = True
        if check == "y":
            return True
        else:
            return False

    def checkFileExists(prompt):
        string = input(" > " + str(prompt) + " ")
        b = os.path.isfile(string)
        while b == False:
            string = input(" > File \"{}\" does not exist. Please re-enter: ".format(string))
            b = os.path.isfile(string)

        string = string.strip()
        return string

    def numberInput(prompt,range=""):
        if range != "":
            range = str(range)
            range = range.split(":")
            numType = str(range[2])
            if numType == "whole":
                lower = int(range[0])
                upper = int(range[1])
            else:
                lower = float(range[0])
                upper = float(range[1])

            number = lower - 1
            while (number < lower) or (number > upper):
                number = input(
                    " > " + prompt + " (" + str(lower) + " through " + str(upper) + "): ")
                try:
                    if numType == "float":
                        number = float(number)
                    elif numType == "whole":
                        number = int(number)
                except:
                    print("No valid number entered! Please try again...")
                    number = lower - 1
                else:
                    if numType == "float" and type(number) is float:
                        if number < lower or number > upper:
                            print("Allowed values are " + float(lower) + " through " + float(upper) + ". Please try again.")
                        else:
                            return number
                    elif numType == "whole" and type(number) is int:
                        if number < lower or number > upper:
                            print("Allowed values are " + str(lower) + " through " + str(upper) + ". Please try again.")
                        else:
                            return number
        else:
            while 1:
                number = input(" > " + prompt + " (numeric entry): ")
                try:
                    number = float(number)
                except:
                    print("No valid number entered! Please try again...")
                else:
                    return number


    if inType != "":
        inType = inType.lower()

    if inType == "":
        input(" > " + str(message) + " ")
        return 0
    elif inType == "yn":
        return yesNoPrompt(message)
    elif inType == "string":
        return stringInput(message)
    elif inType == "file":
        return checkFileExists(message)
    elif inType == "num":
        return numberInput(message,range)
# 
# 
# rate = userPrompt("Enter the baud rate of the serial port","num")
# print(rate)