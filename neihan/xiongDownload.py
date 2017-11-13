# -- coding: UTF-8 -- 
import sys
import os
import os.path
import urllib
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

f = open("xiong.json")
urlList=json.load(f)
# print urlList
for index,url in enumerate(urlList):
	print url['url']
	print index+1
	downloadUrl=url['url']
	title=index+1
	path='/Volumes/my/内涵段子/胸/%s.mp4'%title
	urllib.urlretrieve(downloadUrl, path)    
