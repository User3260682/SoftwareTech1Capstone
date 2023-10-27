#Import Everything
from tkinter import *

root = Tk()
root.title("File Text Writing System")

#Initialise variables:
InputVar1 = IntVar
InputVar2 = IntVar

ListText = []

def DisplayValues():  
    wordnum = int(Entry_1.get())
    W = int(0)
    
    while W < wordnum:
        Label_2 = Label(root, text="Enter Word Number"+str(W+1)+":")      
        Entry_2 = Entry(root, textvariable=InputVar2)
        Label_2.grid(row=(W+2), column=2)
        Entry_2.grid(row=(W+2), column=3)
        W+=1

    Button_2 = Button(root, text="Write", command=WriteToFile)
    Button_2.grid(row=2, column=0)

def WriteToFile():
    wordnum = int(Entry_1.get())
    words_1 = []
    i = int(0)
    
    while i < wordnum:
        widget = root.grid_slaves(row=(i+2), column=3)
        words_1.append(widget[0].get())
        i += 1

    words_2 = []
    j = int(0)
    while j < len(words_1):
        words_2.append(str(words_1[j])+"\n")
        j+=1

    with open("file.txt", "w") as file:
        file.writelines(words_2)
        file.close

borderlabel1 = Label(root, text=" ")
borderlabel2 = Label(root, text=" ")
borderlabel3 = Label(root, text=" ")
borderlabel4 = Label(root, text=" ")
        
Label_1 = Label(root, text="Enter Number of words")
Entry_1 = Entry(root, textvariable=InputVar1)
Button_1 = Button(root, text="Confirm", command=DisplayValues)

borderlabel1.grid(row=0, column=0)
borderlabel2.grid(row=0, column=1)
borderlabel3.grid(row=4, column=4)
borderlabel4.grid(row=4, column=5)

Label_1.grid(row=1, column=2)
        
Entry_1.grid(row=1, column=3)

Button_1.grid(row=1, column=0)

root.mainloop()
