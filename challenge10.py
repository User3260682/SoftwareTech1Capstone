from tkinter import *
import Challenge9Classes as CL

root = Tk()
root.title("Books Lmao")


def ShowLib():
    i = int(0)
    Label_4 = Label(root, text="Item Name:")
    Label_5 = Label(root, text="Author:")
    Label_6 = Label(root, text="Publisher:")

    Label_4.grid(row=4, column=1)
    Label_5.grid(row=4, column=2)
    Label_6.grid(row=4, column=3)

    while i < len(LibraryItems):
        Label_7 = Label(root, text=str(LibraryItems[i].ItemName))
        Label_8 = Label(root, text=str(LibraryItems[i].Author))
        Label_9 = Label(root, text=str(LibraryItems[i].Publisher))
        Label_7.grid(row=(i + 5), column=1)
        Label_8.grid(row=(i + 5), column=2)
        Label_9.grid(row=(i + 5), column=3)
        i += 1


def ShowBooks():
    i = int(0)
    Label_10 = Label(root, text="Item Name:")
    Label_11 = Label(root, text="Author:")
    Label_12 = Label(root, text="Publisher:")
    Label_13 = Label(root, text="Pages:")
    Label_14 = Label(root, text="Hard Copy:")
    Label_15 = Label(root, text="E Book:")

    Label_10.grid(row=4, column=5)
    Label_11.grid(row=4, column=6)
    Label_12.grid(row=4, column=7)
    Label_13.grid(row=4, column=8)
    Label_14.grid(row=4, column=9)
    Label_15.grid(row=4, column=10)

    while i < len(LibraryBooks):
        Label_16 = Label(root, text=str(LibraryBooks[i].Title))
        Label_17 = Label(root, text=str(LibraryBooks[i].Author))
        Label_18 = Label(root, text=str(LibraryBooks[i].Publisher))
        Label_19 = Label(root, text=str(LibraryBooks[i].Pages))
        Label_20 = Label(root, text=str(LibraryBooks[i].IsHardCopy))
        Label_21 = Label(root, text=str(LibraryBooks[i].IsEbook))
        Label_16.grid(row=(i + 5), column=5)
        Label_17.grid(row=(i + 5), column=6)
        Label_18.grid(row=(i + 5), column=7)
        Label_19.grid(row=(i + 5), column=8)
        Label_20.grid(row=(i + 5), column=9)
        Label_21.grid(row=(i + 5), column=10)
        i += 1


Object_LibraryItem1 = CL.LibraryItemInfo("Title1", "Author1", "Publisher1")
Object_LibraryItem2 = CL.LibraryItemInfo("Title2", "Author2", "Publisher2")
Object_LibraryItem3 = CL.LibraryItemInfo("Title3", "Author3", "Publisher3")
Object_Book = CL.Book("Book Title", "Book Author", "Book Publisher", 15, False, True)

LibraryItems = [Object_LibraryItem1, Object_LibraryItem2, Object_LibraryItem3]
LibraryBooks = [Object_Book]

Label_1 = Label(root, text="Library Directory:")
Label_2 = Label(root, text="Library Item Info:")
Label_3 = Label(root, text="Books:")

Button_1 = Button(root, text="Confirm", command=ShowLib)
Button_2 = Button(root, text="Confirm", command=ShowBooks)

Label_1.grid(row=1, column=4)
Label_2.grid(row=2, column=2)
Label_3.grid(row=2, column=8)
Button_1.grid(row=3, column=2)
Button_2.grid(row=3, column=8)

mainloop()
