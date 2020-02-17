def queryVisa(instrument, command, sFunc=""):
    import pyvisa as visa
    command = str(command)
    msmt = ""
    try:
        msmt = (instrument.query(command))
    except:
        pass
    if msmt.startswith('\"') and msmt.endswith('\"'):
        msmt = msmt[1:-1]
    # msmt = float(msmt)
    msmt = msmt.strip()

    if sFunc != "":
        sFunc = sFunc.lower()

        if sFunc == "float":
            msmt = float(msmt)

    return msmt

def writeVisa(instrument, command):
    inst = instrument
    inst.write(command)

def visaResource(deviceName,searchString=""):
    import pyvisa as visa
    global rm
    global list
    global resources
    global inst

    searchString = searchString.lower()

    rm = visa.ResourceManager()
    list = rm.list_resources()  # Place the resources into tuple "List"
    resources = []  # Prep for the tuple to be converted "resources" from "list"

    for i, a in enumerate(list):  # Enumerate through the tuple "list"
        resources.append(a)  # Place the current enumeration into the indexed spot of "resources"

    if searchString != "":
        inst = ""
        x = 0
        for index, i in enumerate(resources):  # Enumerate through list "resources"
            currentString = i.lower()
            tempSearch = currentString.find(searchString)
            # print("{} - {} - {}".format(i, searchString, tempSearch))

            if tempSearch == 0:
                inst = rm.open_resource(resources[index])
        if inst == "":
            print("Could not find GPIB resource containing: {}".format(searchString))
            return "Could not find GPIB resource containing: {}".format(searchString)
    else:
        print("Detected VISA resources")
        print("=========================================================")

        x = 0
        for i in resources:  # Enumerate through list "resources"
            print('Resource ' + str(x) + ': ' + i)  # Print each resource contained in list "resources"
            x += 1  # X is used to itemize and index the list that gets printed
        print("Resource " + str(x) + ': The GPIB address of my instrument was not auto-detected')
        print("=========================================================")

        address = -1
        while (address < 0) or (address > (x)):
            try:
                address = int(input(
                    " > Enter the resource number of the " + str(deviceName) + " (0 through " + str(x) + "): "))
            except ValueError:
                print("No valid integer entered! Please try again ...")
            if address < 0 or address > (x):
                print("Available resources are 0 through " + str(x) + ". Please try again.")

        if address == x:
            address = GPIB_User_Entry(deviceName)
            inst = rm.open_resource(address)
            del inst.timeout
            return inst
        else:
            inst = rm.open_resource(resources[address])
            del inst.timeout
            return inst
    return inst

def GPIB_User_Entry(deviceName):
    global rm
    global list
    global resources
    global inst

    address = -1
    while (address < 1) or (address > 32):
        try:
            address = int(input(
                " > Enter the GPIB address of the " + str(deviceName) + " (1 through 32): "))
        except ValueError:
            print("No valid integer entered! Please try again ...")
        if address < 1 or address > 32:
            print("Available GPIB addresses are 1 through 32. Please try again.")


    address = str(address)
    address = "GPIB0::" + address + "::INSTR"

    return address

# deviceName = "Test Device"
#
# genVisa = GPIB_resource(deviceName,searchString="GPIB0::5::INSTR")
#
#
# response = queryVisa(genVisa,"*IDN?")
# print("Device " + str("test DUT") + ": "+str(response))
