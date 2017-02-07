import PyPDF2
import requests
import glob
import fnmatch
from gui import *
from reportlab.pdfgen import canvas
import os

technologies = ["Java","php", "c", "Oracle","jdbc","servlet", "C++", "English","hibernate", "HTML", "javascript", "Django","k"]
list1 = [element.lower() for element in technologies]
my_file = open("out.txt", "w")

class mainClass:
    current_dir = ""
    c = canvas.Canvas('test.pdf')
    def set_current_dir(self, dir_name):
        print dir_name
        self.current_dir = dir_name

    def readfile(self, filename):
        file1 = open(filename, 'rb')
        reader = PyPDF2.PdfFileReader(file1)
        allText = ""
        for i in xrange(reader.getNumPages()):
            page = reader.getPage(i)
            text = page.extractText()
            allText += text
        return allText

    def getFullName(self, output,fileName):
        try:
            for dataDict in output["entity_list"]:
                sem = dataDict["sementity"]
                type = sem['type']
                if "FullName" in type:
                    print "Its a Full Name "
                    print dataDict["form"]
                    my_file.write("\n" + dataDict["form"] + " ----> ")
                    break
        except :
            my_file.write("\nError In PDF  " +fileName)

    def init(self, fileText):
        url = 'https://api.meaningcloud.com/topics-2.0'
        params = {'key': '68e2c85289a717e6e2ff583c2548a529'}
        data = {
            'of': 'json',
            'lang': 'en',
            'tt': 'a',
            'txt': fileText
        }
        r = requests.post(url, params=params, data=data)
        output = r.json()
        return output

    def readPageOne(self, filename):
        file = open(filename, 'rb')
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        text = page.extractText()
        return text

    def words_in_string(self, word_list, a_string):
        word_list = [element.lower() for element in word_list]
        return set(word_list).intersection(a_string.lower().split())


    def start(self):
        if not self.current_dir:
            print "error"
            ec = ExitDilagoueWindow()
            ec.init("ERROR Select a folder")

        fileCount = len(fnmatch.filter(os.listdir(self.current_dir), '*.pdf'))
        if not fileCount:
            ec = ExitDilagoueWindow()
            ec.init("ERROR Selected folder dosen't contain any .PDF file")

        print self.current_dir
        for filename in glob.glob(self.current_dir + '/*.pdf'):
            print "files names :", filename
            pageOneText = self.readPageOne(filename)
            fileText = self.readfile(filename)

            output = self.init(pageOneText)
            self.getFullName(output,filename)

            for word in self.words_in_string(technologies, fileText):
                my_file.write(" " + word + " ")
                print(word)

if __name__ == "__main__":
    try:
        mc = mainClass()
        root = Tk()
        od = openDialog(mc, root)
        root.mainloop()
    except:
        print "Exception occurred"
