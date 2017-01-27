import json
import pickle
from pprint import pprint
#thefile = open('test.txt', 'w')
# with open('C:/Users/mulik_p/Desktop/data.json') as data_file:
#     data = json.load(data_file)
#
# myList = []
# newList = []
# for i in data['itemListElement']:
#     #print i['item']
#     myList.append(i['item'])
# #print myList
#
# for i in myList:
#     newList.append(i['name'])
#
# #print newList
#
# """
# fileObject = open(thefile,'wb')
# pickle.dump(newList,fileObject)
# fileObject.close()
# """
file_Name = "testfile"
# with open(file_Name,'wb') as f:
#      pickle.dump(newList, f)
#
# print newList


def readList():
    fileObject = open(file_Name, 'r')
    b = pickle.load(fileObject)
    #print "datais ",b
    return b
     #pprint(data)