from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
def yesNoGUI(questionStr, windowName=""):
    root = Tk()

    canvas1 = tk.Canvas(root, width=1, height=1)
    canvas1.pack()

    MsgBox = tk.messagebox.askquestion(windowName, questionStr, icon='warning')
    if MsgBox == 'yes':
        # root.destroy()
        # print(1)
        response = True
    else:
        # tk.messagebox.showinfo('Return', 'You will now return to the application screen')
        response = False

    # ExitApplication()
    root.destroy()
    return response

def getFilePath(extensionType,initialDir="",extensionDescription="",multi=False):

    root = Tk()

    canvas1 = tk.Canvas(root, width=1, height=1)
    canvas1.pack()

    if multi == True:
        root.filenames = filedialog.askopenfilenames(initialdir=initialDir, title="Select file",
                                                   filetypes=((extensionDescription, extensionType), ("all files", "*.*")))
        list = root.filenames
    else:
        root.filename = filedialog.askopenfilename(initialdir=initialDir, title="Select file",
                                                   filetypes=((extensionDescription, extensionType), ("all files", "*.*")))
        list = root.filename
    root.destroy()
    return list

def getDirectoryPath(initialDir=""):
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(initialdir=initialDir)
    root.destroy()
    return folder_selected

def popupMsg(msg,popTitle=""):
    popup = tk.Tk()
    popup.wm_title(popTitle)
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def getTextEntry(buttonText="",labelText="",titleText=""):

    root = Tk()
    root.title(titleText)

    mystring = StringVar()
    def getvalue():
        global output

        output = mystring.get()

        root.destroy()
    
    Label(root, text=labelText).grid(row=0, sticky=W)  # label
    Entry(root, textvariable=mystring).grid(row=0, column=1, sticky=E)  # entry textbox

    WSignUp = Button(root, text=buttonText, command=getvalue).grid(row=3, column=0, sticky=W)  # button
  
    root.mainloop()
    return output

def yesNoPrompt(message,titleText=""):

    root = tk.Tk()  # create window

    canvas1 = tk.Canvas(root, width=0, height=0)
    canvas1.pack()

    MsgBox = tk.messagebox.askquestion(titleText, message,
                                       icon='warning')
    if MsgBox == 'yes':
        response = True
        root.destroy()
    else:
        response = False
        root.destroy()

    root.mainloop()
    return response

# Examples:
# Multi File Selection
# filename = guiTools.getFilePath("S:\\callabsolutions\\PS-Cal TEGAM\\PS-Cal_V4 October 2019 Release\\_BlankTemplates",True)


# response = yesNoGUI("test", "Important Question!!!")
# print(response)
#
#
# response = yesNoGUI("test", "A second important question!!!")
# print(response)
#
# print(getFilePath())
#
# time.sleep(3)

# Directory Selection
# selectedDirectory = getDirectoryPath("P:\Misc")

# User Input Button
# print(getTextEntry(buttonText="Continue",labelText="Enter Asset Number",titleText="User Input Box"))

# response = yesNoPrompt("Is this the correct asset number?","Yes No Prompt")

