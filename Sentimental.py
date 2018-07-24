import tkinter
from tkinter import *

import numpy as np


def onclick():
    txt=text.get()
    if (sentilist.__contains__(txt)):
        score=sentilist[txt].split(' ')
    else:
        score = "0 0".split(' ')
    posvar.set(score[0])
    negvar.set(score[1])
    pass


# load doc into memory
def load_doc(filename):
    # print("load_doc")
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

data1=load_doc("psl.txt")
#data=re.split('\n', data1)
sentilist={}
for line in re.split('\n',data1):
    tokens =np.asarray(line.split(' '))
    sentilist[tokens[0]]=' '.join(tokens[1:3])

top = tkinter.Tk()
top.geometry("300x250") #You want the size of the app to be 500x500
top.resizable(0, 0)

pos1=Label(top, text="Enter your word in Punjabi: ")
pos1.pack()

text = Entry(top, bd =5)
text.pack()

B = Button(top, text ="Get Score", command = onclick)
B.pack()

labelframe = LabelFrame(top, text="")
labelframe.pack(fill="both", expand="yes")

posvar = StringVar()
pos1=Label(labelframe, text="Positive Score: ")
pos1.pack()
pos = Label(labelframe, textvariable=posvar, text="")
pos.pack()

negvar = StringVar()
neg1=Label(labelframe, text="Negative Score: ")
neg1.pack()
neg = Label(labelframe, textvariable=negvar,text="")
neg.pack()

# Code to add widgets will go here...
top.mainloop()