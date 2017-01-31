import tkFileDialog
from Tkinter import *
from main import *


class openDialog(Frame):
    dir_path = ""
    mc = None

    def __init__(self, mc, master=None):
        master.minsize(width=666, height=60)
        self.root = master
        self.createWidgets()
        self.mc = mc

    def createWidgets(self):
        self.fFrame = Frame(self.root)
        self.svDir = StringVar()
        self.eDir = Entry(self.fFrame, width=70, textvariable=self.svDir)
        self.eDir.pack()
        self.bSelDir = Button(self.fFrame, text="select dir")
        self.filterResume = Button(self.fFrame, text="filter resume")
        self.bSelDir["command"] = self.getDir
        self.filterResume["command"] = self.filter
        self.filterResume.pack(side=LEFT)
        self.bSelDir.pack(side=LEFT)
        self.fFrame.pack()

    def getDir(self):
        global dir_path
        self.dir = tkFileDialog.askdirectory()
        self.svDir.set(self.dir)
        dir_path = self.dir
        self.mc.set_current_dir(dir_path)

    def getCurrentDir(self):
        return dir_path

    def filter(self):
        self.mc.start()
        print "in filter function"
