# -*- coding: utf-8 -*-

import os
import sys
def bianli(path):
    mylist=[]
    nameList=os.listdir(path)
    for filename in nameList:
        filepath=path+'/'+filename
        if filepath==path+'/.DS_Store':
            continue
        print filename

# dicPath=raw_input('输入路径：\n')
# bianli(dicPath)
if __name__ == '__main__':
	# dicPath=raw_input('')
	# print dicPath
	# bianli(dicPath)
    # print bianli('/Volumes/my/gdg')
    print 'test'