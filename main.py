import PyPDF2
import requests
import glob
from readTech import *

technologies = ["Java", "c", "Oracle", "C++", "English", "HTML", "javascript"]
#technologies = readList()
my_file = open("out.txt", "w")

def readfile(filename):
    file1 = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(file1)
    allText = ""
    for i in xrange(reader.getNumPages()):
        page = reader.getPage(i)
        text = page.extractText()
        allText += text
    return allText

def getFullName(output):
    for dataDict in output["entity_list"]:
        sem = dataDict["sementity"]
        type = sem['type']
        if "FullName" in type:
            print "Its a Full Name "
            print dataDict["form"]
            my_file.write("\n"+dataDict["form"]+" ----> ")
            break


def init(fileText):
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

def readPageOne(filename):
    file = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    text = page.extractText()
    return text

# if __name__ == "__main__":
def start():
    for filename in glob.glob('C:/Users/mulik_p/Desktop/resumes/*.pdf'):


        #my_file.write("Hello world")
        print "files names :", filename
        pageOneText = readPageOne(filename)
        fileText = readfile(filename)
        output = init(pageOneText)
        getFullName(output)
        for tech in technologies:
            var = str(tech)
            if var.encode('utf-8').lower() in fileText.lower():
                print "found ",tech
                my_file.write(" "+tech+" ")



