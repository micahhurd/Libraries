def timerFunction(qtyTime, gui="", debug=False):
    # qtyTime is in seconds
    # debug = false is for running in windows terminal
    # debug = true is for program testing inside pycharm
    import time
    import math

    secondsWait = qtyTime
    while secondsWait >= 0:
        minutes = secondsWait / 60
        wholeMinutes = math.floor(minutes)
        seconds = secondsWait - (wholeMinutes * 60)
        if seconds < 10:
            seconds = "0" + str(seconds)
            seconds = seconds.replace(".0", "")
        else:
            seconds = str(seconds)
            seconds = seconds.replace(".0", "")
        if wholeMinutes < 10:
            wholeMinutes = "0" + str(wholeMinutes)
        if gui == "":
            if debug == True:
                print("Minutes Remaining: {}:{}".format(wholeMinutes, seconds))
            else:
                print("Minutes Remaining: {}:{}    \r".format(wholeMinutes, seconds), end="")

        secondsWait -= 1
        time.sleep(1)
    print()


# qtyTime = 7000
# timerFunction(qtyTime, debug=True)
# timerFunction(qtyTime, gui="", debug=True)