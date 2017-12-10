# -- coding: UTF-8 -- 
import os
import sys
path='/Volumes/my/gdg'
namelist=os.listdir(path)
for fileM in namelist:
	if '郭德纲' not in fileM:
		os.remove(path+'/'+fileM)
		print ('删除非')