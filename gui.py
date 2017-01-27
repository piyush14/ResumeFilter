import tkFileDialog
from Tkinter import *
from main import *

class openDialog(Frame):
    def __init__(self, master=None):
        master.minsize(width=666, height=60)
        self.root = master
        self.createWidgets()

    def createWidgets(self):
        self.fFrame = Frame(self.root)
        self.svDir = StringVar()
        self.eDir = Entry(self.fFrame, width=70, textvariable=self.svDir)
        self.eDir.pack()
        self.bSelDir = Button(self.fFrame, text="select dir")
        self.filterResume = Button(self.fFrame, text="filter resume" )
        self.bSelDir["command"] = self.getDir
        self.filterResume["command"] = self.filter
        self.filterResume.pack(side=LEFT)
        self.bSelDir.pack(side=LEFT)
        self.fFrame.pack()

    def getDir(self):
        self.dir = tkFileDialog.askdirectory()
        self.svDir.set(self.dir)
        print self.dir

    def filter(self):
        start()
        print "in filter function"


if __name__ == "__main__":
    root = Tk()
    od = openDialog(root)
    root.mainloop()

