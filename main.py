import PyPDF2
import requests
import glob
from gui import *
from reportlab.pdfgen import canvas

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

    def getFullName(self, output):
        for dataDict in output["entity_list"]:
            sem = dataDict["sementity"]
            type = sem['type']
            if "FullName" in type:
                print "Its a Full Name "
                print dataDict["form"]
                my_file.write("\n" + dataDict["form"] + " ----> ")
                break

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
        print self.current_dir
        for filename in glob.glob(self.current_dir + '/*.pdf'):
            print "files names :", filename
            pageOneText = self.readPageOne(filename)
            fileText = self.readfile(filename)
            # print "filetext", fileText
            splittedText = fileText.split(" ")
            # list2 = [element.lower() for element in splittedText]

            output = self.init(pageOneText)
            self.getFullName(output)

            for word in self.words_in_string(technologies, fileText):
                my_file.write(" " + word + " ")
                print(word)

                # for tech in technologies:
                #     var = str(tech)
                #     if tech.lower() in fileText.lower():
                #         print "found ", tech
                #         my_file.write(" " + tech + " ")
                #  if var.encode('utf-8').lower() in fileText.lower():
                #  print var.encode('utf-8').lower()
                # print "found ", tech
                #  my_file.write(" " + tech + " ")


if __name__ == "__main__":
    mc = mainClass()
    root = Tk()
    od = openDialog(mc, root)
    root.mainloop()
