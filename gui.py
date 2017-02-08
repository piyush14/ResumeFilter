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
        self.root.title("FILTER RESUME")

        self.selDirLable  = Label(self.fFrame, text="Select Path of resume Folder")
        self.selDirLable.pack()
        self.svDir = StringVar()
        self.eDir = Entry(self.fFrame, width=70, textvariable=self.svDir)
        self.eDir.pack()

        self.bSelDir = Button(self.fFrame, text="select dir")
        self.filterResume = Button(self.fFrame, text="filter resume")
        self.bSelDir["command"] = self.getDir
        self.filterResume["command"] = self.filter
        self.filterResume.pack(side=LEFT, padx=70, pady=5)
        self.bSelDir.pack(side=LEFT, padx=0, pady=5)
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

        ec = ExitDilagoueWindow()
        ec.init("\tFINISHED : Output file created on DESKTOP\t ", "exit")


class ExitDilagoueWindow:
    def build(self, master, action):
        frame = Frame(master)
        frame.pack()
        if action == "close":
            button = Button(frame,
                            text=" CLOSE ", fg="red",
                            command=master.destroy)

        if action == "exit":
            button = Button(frame,
                            text=" EXIT ", fg="red",
                            command=quit)

        button.pack(side=LEFT)

    def closeFunction(self,root):
        root.destroy()
        top = Toplevel()
        print "show"

    def init(self, message, action):
        root = Tk()

        if action == "close":
            root.title("ERROR")

        if action == "exit":
            root.title("COMPLETE")

        label = Label(root, fg="BLACK")
        label.pack()
        label.config(text=str(message))
        self.build(root, action)
        root.mainloop()
