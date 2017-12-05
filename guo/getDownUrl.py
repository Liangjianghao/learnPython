# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import json
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# url='http://180.153.255.6/mobile/v1/album/ts-1508311063604?albumId=2667276&device=iPhone&pageSize=20000&source=3&trackId=16205993'
url='http://mobile.ximalaya.com/mobile/v1/album/ts-1508993720860?albumId=5488545&device=iPhone&pageSize=200&searchpage=2&source=3&statEvent=pageview%2Falbum%405488545&statModule=%E4%B8%93%E8%BE%91_%E7%9B%B8%E5%85%B3&statPage=search%40%E4%B8%93%E8%BE%91&statPosition=2&trackId=26819350'

response=requests.get(url).content

# print response
jsonData = json.loads(response)
listArr = jsonData['data']['tracks']['list']

for detail in listArr:
	print detail['title']+detail['playUrl64']
	title=detail['title'].replace('/','、');
	path='/Volumes/my/苗阜/%s.mp3'%title
	print path
	# urllib.urlretrieve(detail['playUrl64'], path)    
