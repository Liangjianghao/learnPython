#无法循环
# -*- coding: utf-8 -*-

import os
import eyed3
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

def test(path):
    mylist=[]
    nameList=os.listdir(path)
    for filename in nameList:
        mylist.append(filename)
    return mylist

# def findAll(path):
# 	mylist=[]
# 	# print len(os.listdir(path))
# 	nameList=os.listdir(path)
#  	for filename in nameList:
# 	    # mp3 =u'%s/%s'%(path,filename)

# 	    print filename
#     	# xx = eyed3.load(mp3)
#     	# print(u'{}时长为：{}秒'.format(filename,xx.info.time_secs))
#     	# time.sleep(10)
#     	# filename=''
#     	mylist.append(filename)
#     return mylist
def timeList(tList):
	for x in tList:
	    mp3 =u'%s/%s'%('/Volumes/my/你要',x)
    	xx = eyed3.load(mp3)
    	print(u'{}时长为：{}秒'.format(x,xx.info.time_secs))
    	time.sleep(10)
    	# filename=''
if __name__ == '__main__':

    # listT=test('/Volumes/my/你要')

    # timeList(listT)


