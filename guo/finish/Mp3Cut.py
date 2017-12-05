# -*- coding: utf-8 -*-
import os
import eyed3
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')


def timej(path):
    xx = eyed3.load(path)
    # print(u'时长为：{}秒'.format(xx.info.time_secs))
    print xx.info.time_secs
    if xx.info.time_secs>1800:
        os.remove(path)


def test(path):
    mylist=[]
    nameList=os.listdir(path)
    for filename in nameList:
        filepath=path+'/'+filename
        print filepath
        if filepath==path+'/.DS_Store':
            continue
        timej(filepath)
        # mylist.append(filepath)
    # return mylist
# print test()

# def findAll(path):
# 	mylist=[]
# 	nameList=os.listdir(path)
#  	for filename in nameList:
#     	mylist.append(filename)
    # return mylist
if __name__ == '__main__':
    print test('/Volumes/my/苗阜')

