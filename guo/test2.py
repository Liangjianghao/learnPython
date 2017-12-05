# -*- coding: utf-8 -*-

import os
import sys
# import bianli
import json
# bianli.bianli('/Volumes/my/gdg')
def bianli(path):
    mylist=[]
    nameList=os.listdir(path)
    for filename in nameList:
        filepath=path+'/'+filename
        if filepath==path+'/.DS_Store':
            continue
        # print filepath
        mylist.append(filepath)
    return mylist
def judgeDic(path):
	if os.path.isdir(path):
	  # print "it's a directory"
	  return True
	elif os.path.isfile(path):
	  # print "it's a normal file"
	  return False
	else:
	  # print "it's a special file (socket, FIFO, device file)"
	  return False

def pathToName(path):
	a = path.split('/')
	# print a
	# print a[len(a)-1]
	return a[len(a)-1]

allList=[]
# allDic=[]
def dicToJson(path):
	name=pathToName(path)
	if judgeDic(path):
		mylist=bianli(path)
		# print mylist
		for dic in mylist:
			if judgeDic(dic):
				# print 'come'+dic
				dicToJson(dic)
			else:
				continue
		allList.append(mylist)
		# allDic['name']=allList
		# return mylist
	else:
		print 'stop'	
	return allList


# dicPath=raw_input('')
resultList=dicToJson('/Users/l/Desktop/1')
# print resultList
# print len(resultList)
# print json.dumps(resultList)
def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))
store(resultList)
# pathToName('/Users/l/Desktop/learnPython')
# it = (1, 2, [30, 40])
# it[2] += [50, 60]
# print(it)

