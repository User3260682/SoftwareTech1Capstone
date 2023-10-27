#Import Everything
from tkinter import *

root = Tk()
root.title("File Text Display System")

lista = []
listb = []
a=0

with open("file.txt", "r") as file:
    line = file.readline()
    for line in file:
        line.replace("/n","")
        lista.append(line)

for n in range(0, len(lista)):
    x = len(lista[n])
    listb.append(x)

for n in range(0, len(listb)):
    a += listb[n]
a /= len(lista)+1

numwords = str(len(lista)+1)
longword = str(lista[listb.index(sorted(listb)[len(listb)-1])])
avgwords = str(a)

print("Number of words in file = "+numwords)
print("The longest word in the file = "+longword)
print("The average length of words in the file = "+avgwords)

Label_1 = Label(root, text="Number of words in file = "+numwords)
Label_2 = Label(root, text="The longest word in the file = "+longword)
Label_3 = Label(root, text="The average length of words in the file = "+avgwords)

Label_1.grid(row=1, column=1)
Label_2.grid(row=2, column=1)
Label_3.grid(row=3, column=1)

mainloop()