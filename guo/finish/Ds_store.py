# -- coding: UTF-8 -- 
import sys
import os
path='/Volumes/my/苗阜二'
namelist=os.listdir(path)
for fileM in namelist:
	print fileM
	if fileM=='.DS_Store':
		print ('存在DS_Store')
		os.remove(path+'/'+'.DS_Store')
		print ('删除DS_Store')