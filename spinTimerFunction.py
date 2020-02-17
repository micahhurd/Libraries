def spinTimerFunction(waitTimeSeconds, message="",debug=False):
    # waitTimeSeconds is in seconds
    # debug = false is for running in windows terminal
    # debug = true is for program testing inside pycharm
    import time
    waitInterval = 0.05
    spinner = 0
    spinQty = round(waitTimeSeconds / waitInterval)
    for j in range(spinQty):
        if spinner == 4:
            spinner = 0
        if spinner == 0:
            progress = "|"
        elif spinner == 1:
            progress = "/"
        elif spinner == 2:
            progress = "-"
        elif spinner == 3:
            progress = "\\"
        time.sleep(waitInterval)
        if debug == False:
            print("{} {}\r".format(message,progress), end="")
        else:
            print("{} {}".format(message, progress))
        spinner += 1

# spinTimerFunction(60,"test",debug=True)